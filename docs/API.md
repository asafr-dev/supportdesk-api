# API overview

API docs (local): [http://localhost:8080/docs](http://localhost:8080/docs)

## Endpoints

- `GET /health`
- `GET /tickets?status=&q=&limit=&offset=`
- `GET /tickets/{id}`
- `PATCH /tickets/{id}/status` body: `{ "status": "in_progress" }`

## Authentication

No auth in this demo API (intentionally simple for fast review).

## Smoke test

```bash
curl -s "http://localhost:8080/health"
curl "http://localhost:8080/tickets?status=open&limit=10"
```
