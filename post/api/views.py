from rest_framework import generics, mixins
from django.db.models import Q
from post.models import Post
from .serializers import PostSerializer

# List, Create and Search view
class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = PostSerializer

    # endpoint for this is http://127.0.0.1:8000/post_api/?q='<look_up>'
    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)
                ).distinct()
        return qs

    # slug field won't show up in POST since we defined it as read_only_fields in PostSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve-Update-Delete Generic API view
class PostRudView(generics.RetrieveUpdateDestroyAPIView): #Detail view
    lookup_field = 'slug' # use get_object(self) method by default
    queryset = Post.objects.all()
    serializer_class = PostSerializer

