from django.db import models

class login_credentials(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.email
