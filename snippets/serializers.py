from rest_framework import serializers
from snippets.models import STYLE_CHOICES,LANGUAGE_CHOICES,Snippet
from django.contrib.auth.models import User


class SnippetSerialiser(serializers.HyperlinkedModelSerializer):
     owner=serializers.ReadOnlyField(source='owner.username')
     highlighted=serializers.HyperlinkedIdentityField(view_name='snippet-highlight')

     class Meta:
        model = Snippet
        fields = ['url','id','owner','title','code','linenos','highlighted','language','style']


class UserSerialiser(serializers.ModelSerializer):
   snippets=serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail",  read_only=True)

   class Meta:
      model=User
      fields=['url','id','username','snippets']