# Lab: Blind SQL injection with time delays (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays)

**Description:** Trigger a ten-second delay through the vulnerable tracking cookie.

**Goal:** Cause a time delay to prove the injection works (usually 10 seconds).

## Official solution summary

The official solution uses the tracking cookie to make query processing take measurably longer. The lab is solved when the response exhibits the specified ten-second delay.

## Defensive takeaways

Treat tracking identifiers as untrusted input and pass them to the database only as bound parameters. Apply request timeouts and monitor unusual latency, but do not rely on timing controls as a substitute for safe query construction.
