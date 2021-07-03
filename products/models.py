from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    url=models.URLField(max_length=200)
    date=models.DateTimeField(null=True)
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    vote=models.IntegerField(default=1)
    body=models.CharField(max_length=150)
    player=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def mod_date(self):
        return self.date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
