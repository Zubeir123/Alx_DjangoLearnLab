# Permissions and Group Setup

## Custom Permissions (on Article model):
- can_view: View article list and details
- can_create: Create new articles
- can_edit: Edit existing articles
- can_delete: Delete articles

## Groups:
- Viewers: Only `can_view`
- Editors: `can_view`, `can_create`, `can_edit`
- Admins: All permissions

## Usage:
- Views are protected using `@permission_required` decorators.
- Users are assigned to groups via Django Admin or programmatically.
- Run `python manage.py setup_permissions` to auto-create groups & assign permissions.
