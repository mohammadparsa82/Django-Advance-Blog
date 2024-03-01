from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers  import PostSerializer
from blog.models import Post


@api_view()
def PostList(request):
    return Response({"name":"mmd"})

@api_view()
def PostDetail(request,id):
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)