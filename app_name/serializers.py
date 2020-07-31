from rest_framework.serializers import Serializer, FileField, ListField

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']


# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(Serializer):
    file_uploaded = ListField(FileField())
    class Meta:
        fields = ['file_uploaded']
