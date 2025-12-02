## Authentication (register, login, logout, profile)

- Register: /register/
- Login: /login/
- Logout: /logout/
- Profile (view/edit): /profile/

Implementation:
- Uses Django's `User` model.
- Registration uses a `RegisterForm` (extends `UserCreationForm`) that includes email.
- Profile editing uses a `ProfileForm` (edits `first_name`, `last_name`, `email`).
- `@login_required` protects profile page.
- All forms include CSRF tokens; messages show feedback.
