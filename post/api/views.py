from rest_framework import generics
from post.models import Post
from .serializers import PostSerializer

#Retrieve-Update-Delete Generic API view
class PostRudView(generics.RetrieveUpdateDestroyAPIView): #Detail view
    lookup_field = 'slug' # use get_object(self) method by default
    queryset = Post.objects.all()
    serializer_class = PostSerializer

