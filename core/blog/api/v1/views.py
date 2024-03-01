from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers  import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404


@api_view(["GET","POST"])
def PostList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view()
def PostDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)