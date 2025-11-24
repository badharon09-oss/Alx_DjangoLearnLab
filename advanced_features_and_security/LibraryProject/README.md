# LibraryProject

This is a Django project created as part of the ALX Django learning tasks.

# Permissions & Group Setup

## Custom Permissions
The `Book` model defines the following permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups (Created in Django Admin)
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → can_view, can_create, can_edit, can_delete

## Protected Views
Views are protected using @permission_required:
- view_books → bookshelf.can_view
- create_book → bookshelf.can_create
- edit_book → bookshelf.can_edit
- delete_book → bookshelf.can_delete

# Security Improvements

## 1. Django Secure Settings
- DEBUG = False
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- X_FRAME_OPTIONS = DENY
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SECURE = True

## 2. CSRF Protection
All forms include {% csrf_token %}.

## 3. Secure ORM Queries
All user inputs are validated with Django forms and ORM filters instead of raw SQL.

## 4. Content Security Policy (CSP)
Added CSP header to restrict external resources and reduce XSS risks.
