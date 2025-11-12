# LLM Copy Format

## Single Endpoint

```markdown
## POST /api/project

Create a new project

**Required Parameters:**
- `projectName` (query, string): Name of the project
- `description` (query, string): Project description

**Request Body:**
Content-Type: application/json

**Example:**
```bash
curl -X POST "https://hopsworks.ai.local/hopsworks-api/api/project" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{...}'
```

**Response:**
Project created successfully
Content-Type: application/json
```

## Full Domain

```markdown
# Hopsworks API - PROJECTS

Base URL: https://hopsworks.ai.local/hopsworks-api
Total endpoints: 38

---

## project

### GET /api/project
Get all projects

### POST /api/project
Create a new project
**Required:** `projectName`, `description`

### GET /api/project/{projectId}
Get project by ID
**Required:** `projectId`
```

Format includes:
- Method + path
- Description
- Required params only
- cURL example
- Response type
