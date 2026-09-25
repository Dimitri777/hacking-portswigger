# Clickjacking - PortSwigger Web Security Academy

Complete solutions and exploits for all Clickjacking labs.

## Labs

### Apprentice
1. [Basic clickjacking with CSRF token protection](01-basic-csrf-protected.md)
2. [Clickjacking with form input data prefilled from a URL parameter](02-prefilled-form-input.md)
3. [Clickjacking with a frame buster script](03-frame-buster-script.md)

### Practitioner
4. [Exploiting clickjacking vulnerability to trigger DOM-based XSS](04-trigger-dom-xss.md)
5. [Multistep clickjacking](05-multistep.md)

## Notes
- Always test positioning with low opacity first (0.1), then set to ~0.0001 for the final attack.
- Victim uses Chrome — test in Chrome.
- Do not click the real "Delete account" button yourself while testing, or the lab will reset.
