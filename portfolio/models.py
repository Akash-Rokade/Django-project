from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="Pics")
    desc=models.TextField()
    offer=models.BooleanField(default=False)
    discount=models.IntegerField()
    price=models.IntegerField()