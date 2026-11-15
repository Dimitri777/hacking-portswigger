# Lab: Visible error-based SQL injection (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based)

**Description:** Use verbose database errors to reveal the administrator's password, then log in.

**Goal:** Extract the administrator password using visible error messages.

## Official solution summary

The tracking cookie reaches a query whose verbose database errors are visible in the response. The official solution uses the error behavior to disclose query results, obtains the administrator's password, and verifies it by logging in through the lab interface.

## Defensive takeaways

Use parameterized queries, suppress internal database details in client-facing errors, and ensure failures do not include query values or result data. Log diagnostic details securely on the server.
