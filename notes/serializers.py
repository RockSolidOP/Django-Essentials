from rest_framework import serializers

from notes.models import Notes

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'text', 'created', 'user')