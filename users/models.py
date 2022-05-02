from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, null=False)
    headline = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
