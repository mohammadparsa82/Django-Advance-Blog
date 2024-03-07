from rest_framework import serializers
from blog.models import Post , Category

"""
class PostSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    status = serializers.BooleanField()
    created_date = serializers.DateTimeField()
    published_data = serializers.DateTimeField() 
"""

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "category",
            "created_date",
            "published_date",
            "status"
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
