from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from AD.models import Admob, CustomAd
from AD.serializers import AdmobSerializer, CustomAdSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def get_admob(request):
    admob = Admob.objects.filter(package_name=request.data['package_name'],
                                 active=True)
    serializer = AdmobSerializer(admob, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_custom(request):
    ads = CustomAd.objects.filter(package_name=request.data['package_name'],
                                  active=True)
    serializer = CustomAdSerializer(ads, many=True)
    return Response(serializer.data)
