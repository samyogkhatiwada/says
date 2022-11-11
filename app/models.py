from django.db import models
# imoprt the User model
from django.contrib.auth.models import User
# create models for confession, comment, and user profile

      
class Confession(models.Model):
    confession = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='confessions')
    def __str__(self):
        return self.confession

