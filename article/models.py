from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(null=False, max_length=100, blank=False)
    time = models.IntegerField(null=False)
    image = models.ImageField(upload_to='images/')
    content = models.TextField(max_length=10000, null=False, blank=False)
    package_name = models.CharField(null=False, max_length=100, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
