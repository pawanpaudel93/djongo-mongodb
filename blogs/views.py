from rest_framework import viewsets

from blogs.serializers import PostSerializer
from blogs.models import Post

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
