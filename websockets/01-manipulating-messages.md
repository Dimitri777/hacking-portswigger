# Lab: Manipulating WebSocket messages to exploit vulnerabilities (Apprentice)

**Lab:** [https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities)

**Task (from PortSwigger):**  
This online shop has a live chat feature implemented using WebSockets.

Chat messages that you submit are viewed by a support agent in real time.

To solve the lab, use a WebSocket message to trigger an `alert()` popup in the support agent's browser.

## Vulnerability
Client-side HTML-encodes `<` before sending. Server reflects the message into the agent's browser without further encoding → XSS if you bypass client encoding via interception.

## Solution

1. Open Live chat and send any message; confirm it appears in **Proxy → WebSockets history**.
2. Send a message containing `<` and observe client-side encoding in the history.
3. Enable WebSocket interception, send another message, and edit the intercepted payload to:

```
<img src=1 onerror='alert(1)'>
```

4. Forward. Alert fires in your browser and in the support agent's browser → lab solved.

## Final Payload
```
<img src=1 onerror='alert(1)'>
```
