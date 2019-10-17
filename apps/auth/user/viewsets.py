from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import UserRotarization
from .serializers import UserRotarizationSerializer


class UserRotarizationCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserRotarization.objects.all()
    serializer_class = UserRotarizationSerializer
    permission_classes = (AllowAny,)
