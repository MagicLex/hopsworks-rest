# Hopsworks API Explorer

Hopsworks API v4.2.0 - 670 endpoints split across 14 domains.

## Quick Start

```bash
python3 -m http.server 8080
open http://localhost:8080
```

Stop server:
```bash
lsof -ti:8080 | xargs kill
```

## Features

- Domain-based navigation
- Search endpoints
- Required vs optional params
- cURL examples
- Copy for LLM (markdown format)

## Structure

```
.
├── index.html              # Domain selector (landing page)
├── explorer.html           # Custom API explorer
├── viewer.html             # Swagger UI fallback
├── split_openapi.py        # Script to split spec by domain
├── specs/                  # Domain-specific OpenAPI files
│   ├── featurestore.json  # 205 endpoints - Feature Store APIs
│   ├── auth.json          # 48 endpoints - Auth & Users
│   ├── admin.json         # 46 endpoints - Admin operations
│   ├── python.json        # 45 endpoints - Python environments
│   ├── alerts.json        # 38 endpoints - Alert management
│   ├── projects.json      # 38 endpoints - Project operations
│   ├── jobs.json          # 31 endpoints - Job execution
│   ├── jupyter.json       # 27 endpoints - Jupyter notebooks
│   ├── git.json           # 23 endpoints - Git integration
│   ├── dataset.json       # 15 endpoints - Dataset operations
│   ├── models.json        # 13 endpoints - Model registry
│   ├── integrations.json  # 8 endpoints - External integrations
│   ├── serving.json       # 6 endpoints - Model serving
│   └── other.json         # 131 endpoints - Utilities
└── hopsworks-api-4.2.0.json # Full spec (backup)
```

## Domains Overview

| Domain | Endpoints | Description |
|--------|-----------|-------------|
| **FeatureStore** | 205 | Feature groups, feature views, training datasets, transformations |
| **Auth** | 48 | Authentication, authorization, API keys, user management |
| **Admin** | 46 | System administration, Kubernetes resources, configuration |
| **Python** | 45 | Python environments, library management, pip commands |
| **Alerts** | 38 | Alert rules, receivers, routes, silences |
| **Projects** | 38 | Project CRUD, members, activities |
| **Jobs** | 31 | Spark/Python jobs, schedules, monitoring |
| **Jupyter** | 27 | Notebook servers, Ray sessions |
| **Git** | 23 | Git repository integration |
| **Dataset** | 15 | File operations, upload, download |
| **Models** | 13 | Model registry, versioning, metadata |
| **Integrations** | 8 | Databricks, Spark, Airflow connectors |
| **Serving** | 6 | Model deployment, inference endpoints |
| **Other** | 131 | Search, messaging, banners, variables |

## Why Split?

Original 780KB spec causes browser timeouts and slow rendering. Split by domain fixes this.

## Source

Original spec: `https://api.swaggerhub.com/apis/hopsworks/hopsworks-api/4.2.0`

## Development

Re-split the spec:
```bash
python3 split_openapi.py
```

The script groups endpoints by analyzing tags and URL patterns.

## LLM Copy

Two copy modes:

- Per endpoint: Required params, cURL example, response type
- Full domain: All endpoints in condensed format

Format: Markdown. See `EXAMPLE_LLM_FORMAT.md`.
