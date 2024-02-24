from django.db import models
from members_app.models import UserEnrollment


class Course(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_name"
            )]

    enrolled_users = models.ManyToManyField(UserEnrollment)
    name = models.CharField(max_length=255)
