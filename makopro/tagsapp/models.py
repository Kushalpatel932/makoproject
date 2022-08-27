from django.db import models

# Create your models here.
class user_register(models.Model):
    username=models.CharField(max_length=200)
    useremail = models.EmailField()
    userphone = models.IntegerField()
    

    def __str__(self):
        return self.username
