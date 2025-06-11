from rest_framework import viewsets
from .models import CV, CVInfo
from .serializers import CVSerializer, CVInfoSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    parser_classes = (MultiPartParser, FormParser)


class CVInfoViewSet(viewsets.ModelViewSet):
    queryset = CVInfo.objects.all()
    serializer_class = CVInfoSerializer

    # def get_queryset(self):
    #     cv_id = self.kwargs.get('cv_id')
    #     if cv_id:
    #         return self.queryset.filter(cv_id=cv_id)
    #     return self.queryset
