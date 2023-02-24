from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny

from music.models import Music

from .filters import MusicFilter
from .paginations import MyOffsetPagination
from .permissions import IsAdminOrReadOnly
from .serializers import MusicSerializer


# music api views

class MusicsList(ListCreateAPIView):
    """Music list"""

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filterset_class = MusicFilter
    pagination_class = MyOffsetPagination
    permission_classes = [AllowAny]


class MusicDetail(RetrieveUpdateDestroyAPIView):
    """Music update-destroy"""

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAdminOrReadOnly]
