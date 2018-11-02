from rest_framework import serializers
from post.models import Post

# ModelSerializer serializes (converts) Model data fields into Json, it also validates the data
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                  'slug',
                  'title',
                  'description',
                  'created',]
