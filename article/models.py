from django.db import models


# Create your models here.

class Article(models.Model):
    class LocaleChoices(models.TextChoices):
        fa_IR = 'fa_IR'
        en_US = 'en_US'
    title = models.CharField(null=False, max_length=100, blank=False)
    time = models.IntegerField(null=False)
    image = models.ImageField(upload_to='images/')
    content = models.TextField(max_length=10000, null=False, blank=False)
    package_name = models.CharField(null=False, max_length=100, blank=False)
    locale = models.CharField(max_length=100, choices=LocaleChoices.choices, default=LocaleChoices.en_US)

    created_at = models.DateTimeField(auto_now_add=True)
