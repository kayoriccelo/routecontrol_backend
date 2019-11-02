from ...core.viewsets import BaseViewSet
from .models import Scripting
from .serializers import ScriptingSerializer


class ScriptingViewSet(BaseViewSet):
    queryset = Scripting.objects.all()
    serializer_class = ScriptingSerializer
    filter_fields = ('id',)
