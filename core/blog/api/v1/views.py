from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers  import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated


@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
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

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def PostDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successful"},status=status.HTTP_204_NO_CONTENT)