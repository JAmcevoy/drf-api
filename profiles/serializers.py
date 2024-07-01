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


