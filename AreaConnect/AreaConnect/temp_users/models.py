from django.db import models


class RegisteredUser(models.Model):
    email = models.EmailField()
    postal_code = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)

