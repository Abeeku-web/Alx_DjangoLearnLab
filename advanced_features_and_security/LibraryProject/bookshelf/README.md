# Permissions and Groups Setup

## Custom Permissions
- `can_view`: Allows viewing of book entries.
- `can_create`: Allows creation of book entries.
- `can_edit`: Allows editing of book entries.
- `can_delete`: Allows deletion of book entries.

## Groups
- **Editors**: Has `can_edit` and `can_create` permissions.
- **Viewers**: Has `can_view` permission.
- **Admins**: Has all permissions including `can_delete`.

## View Protection
- Use the `@permission_required` decorator to enforce permissions in views.