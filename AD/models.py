from django.db import models

class TypeChoices(models.TextChoices):
    BANNER = 'banner'
    INTERSTITIAL = 'interstitial'
    REWARDED = 'rewarded'


class Admob(models.Model):
    type = models.CharField(choices=TypeChoices.choices, max_length=20)
    code = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    package_name = models.CharField(null=False, max_length=100, blank=False)


class CustomAd(models.Model):
    type = models.CharField(choices=TypeChoices.choices, max_length=20)
    content = models.FileField(upload_to='ads/')
    active = models.BooleanField(default=True)
    redirect_url = models.URLField(blank=True, null=True)
    package_name = models.CharField(null=False, max_length=100, blank=False)



