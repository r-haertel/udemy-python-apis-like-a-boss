from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListAPIView):
    querySet = Post.object.all()
    serializer_class = PostSerializer
