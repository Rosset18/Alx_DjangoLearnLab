from django.db import models

class YourModel(models.Model):  # ← Class definition (line 3)
    title = models.CharField(max_length=200)  # ← Must be indented (line 4)
    description = models.TextField()
    # ... other fields ...
