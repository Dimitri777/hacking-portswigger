# Lab: Visible error-based SQL injection (Practitioner)

**Goal:** Extract the administrator password using visible error messages.

## Technique

Force the database to throw an error that includes the data you want (e.g. via CAST, CONVERT, or XML functions that leak data in the error message).

## Common Payload (Microsoft SQL Server style often)

```
' AND 1=CAST((SELECT password FROM users WHERE username='administrator') AS int)--
```

The error message will contain the password.

For other databases, use similar type conversion errors or EXTRACTVALUE that leaks data.
