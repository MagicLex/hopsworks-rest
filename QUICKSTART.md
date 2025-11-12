# Quick Start

## Launch

```bash
python3 -m http.server 8080
```

Open http://localhost:8080

## Stop

```bash
lsof -ti:8080 | xargs kill
```

## Usage

1. Select domain
2. Click endpoint in sidebar
3. View params, examples, responses
4. Copy for LLM: Single endpoint or full domain

## Files

- `index.html` - Domain selector
- `explorer.html` - API browser
- `specs/` - 14 domain OpenAPI files
- `split_openapi.py` - Re-split spec

No dependencies. Pure HTML/CSS/JS.
