#!/usr/bin/env python3
import json
import re
from collections import defaultdict
from pathlib import Path

# Load the OpenAPI spec
with open('hopsworks-api-4.2.0.json', 'r') as f:
    spec = json.load(f)

# Define domain groupings based on tag patterns
domain_patterns = {
    'FeatureStore': r'^(Featurestore|FeatureGroup|FeatureView|TrainingDataset|StorageConnector|Transformation|Expectation|Validation|Query|Statistics|Kafka|GreatExpectation|OnlineIngestion|Commit|FsQuery|PreparedStatement).*',
    'Jobs': r'^(Jobs|JobAlerts|JobSchedule|DefaultJobConfiguration).*',
    'Models': r'^(Models|Model).*',
    'Projects': r'^(Project|ProjectAlerts|ProjectActivities).*',
    'Dataset': r'^(Dataset|Download|Upload|XAttrs).*',
    'Python': r'^(Python|Environment|Library).*',
    'Admin': r'^(Admin|UsersAdmin|ProjectsAdmin|Kube|CertificateMaterializer|CloudRoleMapping|Configuration).*',
    'Auth': r'^(Auth|JWT|ApiKey|Users|X509|SecurityToken|RoleMapping).*',
    'Alerts': r'^(Alert|Receiver|Route|Silence|Management)Resource$',
    'Jupyter': r'^(Jupyter|JupyterRay).*',
    'Git': r'^(Git).*',
    'Serving': r'^(Serving|ModelInference).*',
    'Integrations': r'^(Integrations|Databricks|Spark|Airflow).*',
    'Other': r'^(OpenSearch|Message|Request|HopsworksAction|Tutorials|TagSchemas|Banner|ComputeResources|Endpoint|Variables).*'
}

# Group tags by domain
tag_to_domain = {}
for tag_obj in spec.get('tags', []):
    tag_name = tag_obj['name']
    matched = False
    for domain, pattern in domain_patterns.items():
        if re.match(pattern, tag_name):
            tag_to_domain[tag_name] = domain
            matched = True
            break
    if not matched:
        tag_to_domain[tag_name] = 'Other'

# Group paths by domain
domain_paths = defaultdict(dict)
domain_tags = defaultdict(set)

for path, methods in spec['paths'].items():
    for method, operation in methods.items():
        tags = operation.get('tags', ['Other'])
        primary_tag = tags[0] if tags else 'Other'
        domain = tag_to_domain.get(primary_tag, 'Other')
        
        if path not in domain_paths[domain]:
            domain_paths[domain][path] = {}
        domain_paths[domain][path][method] = operation
        
        for tag in tags:
            domain_tags[domain].add(tag)

# Create domain stats
print(f"\nDomain breakdown:")
print(f"{'Domain':<20} {'Endpoints':<12} {'Tags'}")
print("-" * 60)
for domain in sorted(domain_paths.keys(), key=lambda d: len(domain_paths[d]), reverse=True):
    print(f"{domain:<20} {len(domain_paths[domain]):<12} {len(domain_tags[domain])}")

# Create output directory
output_dir = Path('specs')
output_dir.mkdir(exist_ok=True)

# Generate spec for each domain
for domain, paths in domain_paths.items():
    domain_spec = {
        'openapi': spec['openapi'],
        'info': {
            **spec['info'],
            'title': f"{spec['info']['title']} - {domain}",
            'description': f"{domain} endpoints from Hopsworks API"
        },
        'servers': spec['servers'],
        'security': spec.get('security', []),
        'tags': [t for t in spec['tags'] if t['name'] in domain_tags[domain]],
        'paths': paths,
        'components': spec.get('components', {})
    }
    
    filename = f"{domain.lower().replace(' ', '-')}.json"
    with open(output_dir / filename, 'w') as f:
        json.dump(domain_spec, f, indent=2)
    
    print(f"✓ Generated specs/{filename} ({len(paths)} endpoints)")

print(f"\n✓ Split complete: {len(domain_paths)} domain files created")
