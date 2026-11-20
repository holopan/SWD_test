from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Classroom
from apis.serializers import ClassroomSerializer, ClassroomDetailSerializer
from apis.filters import ClassroomFilter

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomSerializer