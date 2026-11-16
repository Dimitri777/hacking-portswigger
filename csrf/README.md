# Cross-site request forgery (CSRF) - PortSwigger Web Security Academy

Solutions for all CSRF labs in the CSRF topic.

## Labs

### Apprentice
1. [CSRF vulnerability with no defenses](01-csrf-no-defenses.md)

### Practitioner — token validation flaws
2. [CSRF where token validation depends on request method](02-token-depends-on-method.md)
3. [CSRF where token validation depends on token being present](03-token-depends-on-presence.md)
4. [CSRF where token is not tied to user session](04-token-not-tied-to-session.md)
5. [CSRF where token is tied to non-session cookie](05-token-tied-to-non-session-cookie.md)
6. [CSRF where token is duplicated in cookie](06-token-duplicated-in-cookie.md)

### Practitioner — Referer defenses
7. [CSRF where Referer validation depends on header being present](07-referer-depends-on-presence.md)
8. [CSRF with broken Referer validation](08-broken-referer-validation.md)

### Practitioner / Expert — SameSite
9. [SameSite Lax bypass via method override](09-samesite-lax-method-override.md)
10. [SameSite Strict bypass via client-side redirect](10-samesite-strict-client-redirect.md)
11. [SameSite Lax bypass via cookie refresh](11-samesite-lax-cookie-refresh.md)
12. [SameSite Strict bypass via sibling domain](12-samesite-strict-sibling-domain.md)

Replace `YOUR-LAB-ID` and use a unique email for the victim (not one already registered).
