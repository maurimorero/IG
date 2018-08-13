from rest_framework import serializers
from .models import TwitterProfile, Request


#class UserSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
 #       model = User
  #      fields = ('url', 'username', 'email')

class TwitterProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TwitterProfile
        fields = ('username', 'name', 'description', 'imageURI', 'popularityIndex')

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('username','createdDate','status')