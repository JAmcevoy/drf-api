from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    Why: This serializer converts Profile model instances to JSON and vice versa,
         facilitating serialization and deserialization for API interactions.

    Fields:
        - id: The unique identifier for the profile.
        - owner: Read-only field that retrieves the username of the profile owner.
        - created_at: Timestamp indicating when the profile was created.
        - updated_at: Timestamp indicating when the profile was last updated.
        - name: Name associated with the profile.
        - content: Additional content associated with the profile.
        - image: Image associated with the profile.
    """
    owner = serializers.ReadOnlyField(source='owner.username')  # Retrieves the username of the owner
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile  # Specifies the model to be serialized
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner'
        ]  # Defines the fields to include in the serialized output

# class PostSerializers(serializers.ModelSerializer):
#     """
#     Serializer for the Post model.

#     Why: This serializer converts Post model instances to JSON and vice versa,
#          enabling serialization and deserialization for API interactions.

#     Fields:
#         - id: The unique identifier for the post.
#         - owner: Foreign key field linking to the user who authored the post.
#         - title: Title of the post.
#         - content: Content or body of the post.
#         - image: Image associated with the post.
#         - profile_name: Read-only field that retrieves the name of the profile associated with the post's owner.
#         - profile_image: Read-only field that retrieves the URL of the image associated with the profile of the post's owner.
#     """
#     profile_name = serializers.ReadOnlyField(source='owner.profile.name')  # Retrieves the name of the owner's profile
#     profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')  # Retrieves the URL of the owner's profile image

#     class Meta:
#         model = Post  # Specifies the model to be serialized
#         fields = [
#             'id', 'owner', 'title', 'content', 'image'
#         ]  # Defines the fields to include in the serialized output
