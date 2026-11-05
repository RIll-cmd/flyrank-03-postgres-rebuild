# Postgres task API rebuild

AI-assisted rebuild of flyrank-03-postgres and A1. Original repos/data preserved. Real chronological checkpoints, no hand-built authorship claim.

Requires Docker Desktop. Copy .env.example to .env and replace the example password in both fields. Run `docker compose up --build`. Open http://localhost:8103/docs. Isolated project/volume; database is on localhost:5543.

| Method | Endpoint | Result |
|---|---|---|
| GET | /tasks, /tasks/{id} | 200; 404 missing |
| POST | /tasks | 201; 400 invalid |
| PUT | /tasks/{id} | 200; 400 invalid; 404 missing |
| DELETE | /tasks/{id} | 204; 404 missing |

Tables and three seeds are automatic, only once. Parameterized queries handle CRUD. A named volume preserves tasks across compose down/up. Deleting volumes removes data. The unchanged A1 CRUD checkpoint passing across memory, SQLite and Postgres demonstrates that storage is an implementation detail behind the HTTP contract.

## Requirement checks
- [x] Actual Postgres and one-command Docker full stack checked.
- [x] Ignored .env and committed placeholders; no credentials committed.
- [x] Automatic table and three seeds only once.
- [x] Unchanged A1 CRUD test passes with 200/201/204/400/404 JSON errors.
- [x] Full compose down/up persistence checked at Stage 4.
- [ ] New database screenshot and curl transcript pending.
- [x] Public repo, six exact stage commits, run command, endpoint table.
