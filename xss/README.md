# Cross-site scripting (XSS) - PortSwigger Web Security Academy

Solutions for XSS labs in the XSS topic.

Each of these is self-contained: the lab registers as **Solved** the moment a JavaScript
`alert()` executes in your own browser. No exploit server or victim delivery is needed.

## Labs

### Apprentice — reflected / stored
1. [Reflected XSS into HTML context with nothing encoded](01-reflected-html-context-nothing-encoded.md)
2. [Stored XSS into HTML context with nothing encoded](02-stored-html-context-nothing-encoded.md)

### Apprentice — DOM-based
3. [DOM XSS in document.write sink using source location.search](03-dom-document-write-sink.md)
4. [DOM XSS in innerHTML sink using source location.search](04-dom-innerhtml-sink.md)

### Practitioner — contexts
5. [Reflected XSS into a JavaScript string with angle brackets HTML encoded](05-reflected-js-string-angle-brackets-encoded.md)
