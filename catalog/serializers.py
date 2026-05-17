from rest_framework import serializers
from catalog.models import Newspaper, Topic, Redactor


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name"]


class RedactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redactor
        fields = ["id", "username", "first_name", "last_name", "years_of_experience"]


class NewspaperSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    publishers = RedactorSerializer(many=True, read_only=True)
    topic_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Topic.objects.all(),
        source="topics"
    )
    publisher_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Redactor.objects.all(),
        source="publishers"
    )

    class Meta:
        model = Newspaper
        fields = [
            "id", "title", "content", "published_date",
            "topics", "publishers",
            "topic_ids", "publisher_ids"
        ]