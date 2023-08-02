# AO-Transactions

```sql
-- Read - Modify - Write
SELECT ... FOR UPDATE
```

https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-MODIFYING

### Deadlock
```sql

-- Session 1
BEGIN;
UPDATE users SET balance = balance - 100 WHERE id = 1; -- RowExclusiveLock

-- RowExclusiveLock conflicts with the following:
--   SHARE - CREATE INDEX
--   SHARE ROW EXCLUSIVE - CREATE TRIGGER
--   EXCLUSIVE - REFRESH MATERIALIZED VIEW CONCURRENTLY
--   ACCESS EXCLUSIVE - DROP TABLE, TRUNCATE TABLE, REINDEX TABLE, CLUSTER TABLE, VACUUM FULL

-- Session 2
BEGIN;
UPDATE users SET balance = balance + 100 WHERE id = 2;
UPDATE users SET balance = balance - 100 WHERE id = 1; -- ExclusiveLock

-- ExclusiveLock conflicts with the following:
--   ROW SHARE
--   ROW EXCLUSIVE
--   SHARE UPDATE EXCLUSIVE
--   SHARE
--   SHARE ROW EXCLUSIVE
--   EXCLUSIVE
--   ACCESS EXCLUSIVE

-- Session 1
UPDATE users SET balance = balance - 100 WHERE id = 2; -- Deadlock

```

### SELECT FOR UPDATE
```sql
--Session 2
BEGIN;
SELECT * FROM users WHERE id = 2 FOR UPDATE;
UPDATE users SET balance = balance + 100 WHERE id = 2;

--Session 1
BEGIN;
UPDATE users SET balance = balance - 100 WHERE id = 2; -- Waiting for Session 2 to commit

--Session 2
UPDATE users SET balance = balance + 100 WHERE id = 2;
COMMIT; -- Session 1 releases without UPDATE because the WHERE clause dont match
```


Optimistic Locking
<TBD>
