# Lab: Blind SSRF with out-of-band detection (Practitioner)

**Lab:** [https://portswigger.net/web-security/ssrf/blind/lab-out-of-band-detection](https://portswigger.net/web-security/ssrf/blind/lab-out-of-band-detection)

**Task (from PortSwigger):**  
This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded.

To solve the lab, use this functionality to cause an HTTP request to the public Burp Collaborator server.

**Note:** Use Burp Collaborator’s default public server (firewall blocks arbitrary external systems).

## Vulnerability
Server-side analytics fetches the Referer URL (blind SSRF).

## Solution

1. Product page request → Repeater.
2. Replace `Referer` with a Collaborator payload (right-click → Insert Collaborator payload).
3. Send → Collaborator tab → Poll now → DNS/HTTP interactions confirm the lab is solved.

## Final Payload
```
Referer: https://YOUR-COLLABORATOR-SUBDOMAIN.oastify.com
```
