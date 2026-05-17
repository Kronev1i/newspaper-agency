from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from catalog.models import Newspaper, Topic, Redactor
from catalog.serializers import (
    NewspaperSerializer,
    TopicSerializer,
    RedactorSerializer
)


class NewspaperViewSet(viewsets.ModelViewSet):
    """
    API endpoint for newspapers.
    list: Get all newspapers.
    create: Create a new newspaper.
    retrieve: Get a specific newspaper.
    update: Update a newspaper.
    destroy: Delete a newspaper.
    """
    queryset = Newspaper.objects.select_related().prefetch_related(
        "topics", "publishers"
    ).order_by("-published_date")
    serializer_class = NewspaperSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date", "title"]


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint for topics.
    """
    queryset = Topic.objects.all().order_by("name")
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class RedactorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for redactors.
    """
    queryset = Redactor.objects.all().order_by("username")
    serializer_class = RedactorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "first_name", "last_name"]
