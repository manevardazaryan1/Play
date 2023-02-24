from rest_framework import serializers

from music.models import Music

# serializers


class MusicSerializer(serializers.ModelSerializer):
    """Music serializer"""

    class Meta:
        model = Music

        fields = [
            "id",
            "name",
            "genre",
            "audio",
            "year",
            "singer",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "is_published",
        ]
