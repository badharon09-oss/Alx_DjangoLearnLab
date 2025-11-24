# HTTPS Deployment Notes

## SSL/TLS Setup
Ensure the server uses HTTPS with valid SSL certificates:
- For Nginx: use `ssl_certificate` and `ssl_certificate_key` directives.
- Certificates may be generated using Let’s Encrypt.

## Django HTTPS Settings
The following settings enforce HTTPS and security protections:
- SECURE_SSL_REDIRECT
- SECURE_HSTS_SECONDS
- SECURE_HSTS_INCLUDE_SUBDOMAINS
- SECURE_HSTS_PRELOAD
- SESSION_COOKIE_SECURE
- CSRF_COOKIE_SECURE
- X_FRAME_OPTIONS
- SECURE_BROWSER_XSS_FILTER
- SECURE_CONTENT_TYPE_NOSNIFF

These work together to protect from:
- Cookie theft
- Packet sniffing
- Clickjacking
- XSS attacks
- Protocol downgrade attacks
