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
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "snippet",
            "category",
            "status",
            "absolute_url",
            "relative_url",
            "created_date",
            "published_date",
        ]
        #read_only_fields = ['content']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.title)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
