from rest_framework import fields, serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'created']
  
