from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializers

class PostList(APIView):
    serializer_class = PostSerializers
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializers(
            data=request.data, context={'request', request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)