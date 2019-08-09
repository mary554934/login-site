from django.db import models

class Membership(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    login_ID = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def register(self):
        self.save()

    def __str__(self):
        return self.first_name