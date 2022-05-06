from rest_framework import serializers
from .models import Links, LinkList


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkList
        fields = "__all__"
        
        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"
        
        
class GetLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['title', 'link', 'id']
        

