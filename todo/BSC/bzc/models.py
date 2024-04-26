from django.db import models 
from django.contrib.auth.models import User

class todo(models.Model):
    task=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    due=models.DateField()
    uid=models.ForeignKey(User,on_delete=models.CASCADE)