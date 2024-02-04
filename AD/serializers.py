from rest_framework import serializers

from AD.models import Admob, CustomAd


class AdmobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admob
        fields = '__all__'


class CustomAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomAd
        fields = '__all__'