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

Comments Feature
----------------
- Model: blog.Comment (post FK, author FK, content, created_at, updated_at)
- Create: POST to /posts/<post_pk>/comments/new/ (authenticated users only)
- Edit: /comments/<comment_pk>/edit/ (only comment author)
- Delete: /comments/<comment_pk>/delete/ (only comment author)
- Display: comments appear on the Post detail page; a CommentForm is rendered for logged-in users.
- To run migrations: python manage.py makemigrations blog && python manage.py migrate
