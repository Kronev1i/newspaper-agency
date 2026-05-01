from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.forms import RedactorExperienceUpdateForm
from catalog.models import Topic, Newspaper
from django.urls import reverse


class FormTest(TestCase):
    def test_years_of_experience_validation(self):
        form_data = {"years_of_experience": 10}
        form = RedactorExperienceUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {"years_of_experience": -1}
        form = RedactorExperienceUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())


class SearchTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_redactor",
            password="testpassword123"
        )
        self.client.force_login(self.user)

        self.topic = Topic.objects.create(name="IT")
        Newspaper.objects.create(
            title="Django News",
            content="Content",
            topic=self.topic
        )
        Newspaper.objects.create(
            title="Almaty Today",
            content="Content",
            topic=self.topic
        )

    def test_newspaper_search_by_title(self):
        url = reverse("catalog:newspaper-list")
        response = self.client.get(url, {"title": "Django"})
        self.assertContains(response, "Django News")
        self.assertNotContains(response, "Almaty Today")

    def test_topic_search_by_name(self):
        Topic.objects.create(name="Politics")
        url = reverse("catalog:topic-list")
        response = self.client.get(url, {"name": "Poli"})
        self.assertContains(response, "Politics")
        self.assertNotContains(response, "IT")