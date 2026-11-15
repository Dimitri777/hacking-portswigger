# Lab: Blind SQL injection with time delays and information retrieval (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)

**Description:** Infer the administrator's password from conditional response delays and use it to log in.

**Goal:** Extract the administrator password using time-based blind SQLi.

## Official solution summary

The lab's PostgreSQL-backed query can be made to respond slowly only when a tested condition is true. The official solution uses this timing difference to infer the administrator's password, then verifies the credentials by logging in through the lab interface.

## Defensive takeaways

Use parameterized queries for analytics values and avoid letting user-controlled input affect query execution time. Monitor repeated requests with unusual latency and rate-limit abusive patterns.
