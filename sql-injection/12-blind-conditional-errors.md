# Lab: Blind SQL injection with conditional errors (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors)

**Description:** Use conditional database errors to infer the administrator's password and log in.

**Goal:** Extract administrator password via error-based blind SQLi.

## Official solution summary

This lab uses Oracle. The official solution relies on a detectable difference between a normal response and a database error to infer whether a tested condition is true. Repeating this process reveals the administrator's password, which is then verified by logging in through the lab interface.

## Defensive takeaways

Use parameterized queries and return uniform, generic error responses to clients. Keep detailed database diagnostics in access-controlled server logs rather than exposing them in HTTP responses.
