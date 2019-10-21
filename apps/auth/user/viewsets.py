from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import UserRotarization
from .serializers import UserRotarizationCreateSerializer, UserRotarizationSerializer


class UserRotarizationCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserRotarization.objects.all()
    serializer_class = UserRotarizationCreateSerializer
    permission_classes = (AllowAny,)

class UserRotarizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserRotarization.objects.all()
    serializer_class = UserRotarizationSerializer

    def get_queryset(self):
        return  UserRotarization.objects.filter(cpf=self.request.user.cpf)
