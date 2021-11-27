from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
    queryset = Post.objects.all()
    serializer_class = PostSerializer
