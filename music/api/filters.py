from django_filters import FilterSet, NumberFilter

from music.models import Music

# filters


class MusicFilter(FilterSet):
    """Music model filter class"""

    class Meta:
        model = Music

        min_year = NumberFilter(
            field_name="music__year", lookup_expr="gte")
        max_year = NumberFilter(
            field_name="music__year", lookup_expr="lte")

        fields = {
            "name": ["exact"],
            "genre": ["exact"],
            "audio": ["exact"],
            "singer": ["exact"],
        }
