# Django Security Practices

## Settings
- `DEBUG = False`
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS = 'DENY'`, `CSRF_COOKIE_SECURE = True`

## CSRF
- All forms include `{% csrf_token %}`

## Views
- Inputs are stripped and validated using `full_clean()`
- ORM used instead of raw SQL

## CSP
- Implemented via `django-csp` middleware
- Only trusted sources allowed for styles/scripts

## Manual Testing
- Verified CSRF token present in forms
- Tried submitting malicious HTML/JS — it was blocked
- Confirmed users without permission cannot access protected views
