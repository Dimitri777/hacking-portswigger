# Lab: Blind SQL injection with conditional responses (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)

**Description:** The tracking cookie is included in a database query. The page shows a "Welcome back" message when that query returns a row. The goal is to infer the administrator's password and log in.

**Goal:** Find the password of the `administrator` user (usually 20 characters, lowercase + numbers).

**Tracking cookie:** Vulnerable to injection.

## Official solution summary

The official solution uses the difference in page content as a yes/no signal. It tests facts about the administrator account and password until the credentials are known, then verifies them by logging in through the lab interface. The password is lowercase alphanumeric.

## Defensive takeaways

Use parameterized queries for analytics identifiers, validate cookie values against the expected format, and avoid response behavior that reveals database query results.
