from rest_framework import viewsets
from .serializers import NotesSerializers
from .models import Notes
# Create your views here.

# View Sets for API

class NotesViewSet(viewsets.ModelViewSet):
   queryset = Notes.objects.all()
   serializer_class = NotesSerializers