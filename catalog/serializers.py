from rest_framework import serializers
from catalog.models import Topic, Newspaper, Redactor


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name"]


class RedactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redactor
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "years_of_experience"
        ]


class NewspaperSerializer(serializers.ModelSerializer):
    # Embedded objects representation for read operations (GET)
    topic = TopicSerializer(read_only=True)
    publishers = RedactorSerializer(many=True, read_only=True)

    # Primary key write-only fields for write operations (POST/PUT)
    topic_id = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(),
        write_only=True,
        source="topic"
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
            "topic", "publishers",
            "topic_id", "publisher_ids"
        ]
