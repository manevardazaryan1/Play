from rest_framework.pagination import LimitOffsetPagination

# pagination


class MyOffsetPagination(LimitOffsetPagination):
    """Pagionation class"""
    default_limit = 10
    max_limit = 20
