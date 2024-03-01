from rest_framework import serializers
from blog.models import Post

"""
    class PostSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField(max_length=255)
        content = serializers.CharField(max_length=255)
        created_date = serializers.DateTimeField()
"""

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "status"
        ]