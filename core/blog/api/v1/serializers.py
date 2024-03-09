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
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = [
            "id",
            "image",
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
        return request.build_absolute_uri(obj.id)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if  request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet',None)
            rep.pop('absolute_url',None)
            rep.pop('relative_url',None)
        else:
            rep.pop('content',None)

        rep['category'] = CategorySerializer(instance.category).data
        return rep
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
