#  Managing Permissions and Groups in Django

##  Objective
Implement and manage permissions and groups to control access to various parts of the Django application. This enhances both functionality and security through role-based access control.

---

i##  Models Configuration

**Model Used:** `Book`

Custom permissions added in `models.py`:

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]

