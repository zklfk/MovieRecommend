from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=32,primary_key=True,unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    register_time = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['register_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'