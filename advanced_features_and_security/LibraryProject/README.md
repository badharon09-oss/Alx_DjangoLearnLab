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
