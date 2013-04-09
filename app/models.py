from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=200, unique=True)
    added = models.DateTimeField(auto_now_add=True)
    f = models.FileField(upload_to="pics", null=False)

class Comments(models.Model):
    name = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    picture = models.ForeignKey(Picture)

