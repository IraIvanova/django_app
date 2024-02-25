from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_name"
            )]

    enrolled_users = models.ManyToManyField(User)
    name = models.CharField(max_length=255)
