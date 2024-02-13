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
    logo = models.FileField(upload_to='ads/')
    rate = models.FloatField(default=4.0)
    name = models.CharField(max_length=100, default='')
    creator = models.CharField(max_length=100, default='')
    total_rate = models.CharField(default='', max_length=100)
    downloads = models.CharField(default='', max_length=100)
    age = models.IntegerField(default=12)
    description = models.TextField(max_length=1000, default='')
    active = models.BooleanField(default=True)
    redirect_url = models.URLField(blank=True, null=True)
    package_name = models.CharField(null=False, max_length=100, blank=False)


class ScreenShot(models.Model):
    ad = models.ForeignKey(CustomAd, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/screenshots/')
