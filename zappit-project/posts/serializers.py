from rest_framework import fields, serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):

    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    class Meta: 
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'posterid', 'created']
  

class VoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vote
        fields = ['id']
