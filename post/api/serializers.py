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
        read_only_fields = ['slug',] # slug field is now read only, cannot be changed by PUT or PATCH

    def validate_title(self, value):
        qs = Post.objects.filter(title__iexact=value)  # including objects(post) with the title=value, this includes the current instance
        print("qs includes instance:" + str(qs))

        # self.instance refer to the instance of the model defined in class Meta, while "self" refers to the the subclass of ModelSerializer, in this case PostSerializer
        if self.instance:
            qs = qs.exclude(id=self.instance.id) # if value is current instance.title means we are not changing anything so we just exclude it from qs
            print("qs after exclude instance: " + str(qs))
        if qs.exists():
            raise serializers.ValidationError('This title has already been used')
        return value