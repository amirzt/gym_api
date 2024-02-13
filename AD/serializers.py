from rest_framework import serializers

from AD.models import Admob, CustomAd, ScreenShot


class AdmobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admob
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenShot
        fields = ['image']


class CustomAdSerializer(serializers.ModelSerializer):
    screen_shots = serializers.SerializerMethodField('get_screens')

    @staticmethod
    def get_screens(self):
        screens = ScreenShot.objects.filter(ad=self)
        return ScreenSerializer(screens, many=True).data

    class Meta:
        model = CustomAd
        fields = '__all__'
