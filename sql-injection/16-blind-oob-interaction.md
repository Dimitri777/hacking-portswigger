# Lab: Blind SQL injection with out-of-band interaction (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band)

**Description:** Cause an out-of-band DNS lookup to Burp Collaborator through the vulnerable tracking cookie.

**Goal:** Trigger an out-of-band DNS/HTTP interaction (Burp Collaborator required).

## Official solution summary

The official solution demonstrates that the vulnerable database query can cause an external DNS interaction. The lab is completed by observing the expected interaction in Burp Collaborator's public service, as required by the Academy environment.

## Defensive takeaways

Use parameterized queries and restrict database network egress to explicitly required destinations. Disable unnecessary database features that permit external lookups, and monitor DNS and outbound requests from database hosts.
