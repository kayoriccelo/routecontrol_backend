from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets

from .serializers import TokenCustomSerializer


class TokenCustomView(TokenObtainPairView):
    serializer_class = TokenCustomSerializer
