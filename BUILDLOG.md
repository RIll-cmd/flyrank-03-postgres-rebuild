
## Stage 0
Command: docker compose exec -T db psql -U tasks -d tasks -c SELECT 1;
Result: ?column? 
----------
        1
(1 row)
