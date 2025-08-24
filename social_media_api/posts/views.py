from rest_framework import generics, viewsets, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList():
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ""

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []


# @api_view(['POST', "GET"])
# def PostBlog(request):
#     if request.method == "POST":
#         print({"request": request.data})
#         print(request.user.id)
#         post = Post.objects.create(author=request.user,title=request.data['title'],content=request.data['content'])
#         """ serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) """
#         #return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#     return Response({'message':"item received"})
    
    
#     """ elif request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data) """
    
# @api_view(['GET'])   
# def listPost(request):
#     post = Post.objects.all()
#     print()

#     return Response({'message':"item recieved"})
    


    


