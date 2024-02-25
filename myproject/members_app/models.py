from django.db import models
from django.contrib.auth.models import User
from courses_app.models import Course


class Member(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_email"
            )]

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

