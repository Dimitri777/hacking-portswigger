# Lab: Blind SQL injection with out-of-band data exfiltration (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration)

**Description:** Retrieve the administrator's password through an out-of-band interaction and use it to log in.

**Goal:** Exfiltrate the administrator password via out-of-band channel (DNS/HTTP to Collaborator).

## Official solution summary

This lab extends out-of-band interaction to demonstrate that query results can influence an external interaction. The official solution retrieves the administrator's password through the lab's required Burp Collaborator service, then verifies the credentials by logging in.

## Defensive takeaways

Do not construct SQL from untrusted input. Restrict outbound network access from database servers, avoid storing credentials in recoverable plaintext, and alert on unexpected external DNS or HTTP traffic.
