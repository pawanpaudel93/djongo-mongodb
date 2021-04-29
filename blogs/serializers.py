from rest_framework import serializers

from blogs.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        lookup_field = "_id"
         