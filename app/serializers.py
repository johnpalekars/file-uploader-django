from app.models import CustomUser
from rest_framework import serializers
from app.models import Files
from django.conf import settings


class DownloadSerializer(serializers.ModelSerializer):

    '''Serializer for download api'''

    class Meta:
        model = Files
        fields = ('fileName', 'fileLocation','fileSize', 'modified')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username' 'email']
        

