
## Stage 0
Command: docker compose exec -T db psql -U tasks -d tasks -c SELECT 1;
Result: ?column? 
----------
        1
(1 row)

## Stage 1
Command: C:\Python314\python.exe checkpoint.py
Result: PASS env connection, automatic table and exactly three seeds after restart

## Stage 2
Command: C:\Python314\python.exe checkpoint.py
Result: PASS Postgres list, single, missing 404
