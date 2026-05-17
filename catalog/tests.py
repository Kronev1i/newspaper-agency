from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from catalog.models import Topic, Newspaper

# ==============================================================================
# 1. DJANGO CORE TESTS (MODELS AND HTML VIEWS)
# ==============================================================================


class DjangoCoreTests(TestCase):
    def setUp(self):
        # Initializes fresh,
        # isolated test database records before each test case
        self.user = get_user_model().objects.create_user(
            username="test_redactor",
            password="securepassword123",
            years_of_experience=3
        )
        self.topic = Topic.objects.create(name="Business")
        self.newspaper = Newspaper.objects.create(
            title="Wroclaw Business Journal",
            content="IT market is growing dynamically.",
            topic=self.topic
        )
        self.newspaper.publishers.add(self.user)

    def test_topic_str(self):
        """
        Verify that the string representation
        of the Topic model is correct
        """
        self.assertEqual(str(self.topic), "Business")

    def test_newspaper_list_view_login_required(self):
        """Verify that anonymous users are redirected to the login page"""
        url = reverse("catalog:newspaper-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_newspaper_list_view_authenticated(self):
        """
        Verify that authenticated users
        can access the list view and see content
        """
        self.client.login(
            username="test_redactor",
            password="securepassword123"
        )
        url = reverse("catalog:newspaper-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Wroclaw Business Journal")


# ==============================================================================
# 2. DRF API ARCHITECTURE TESTS
# ==============================================================================

class ApiArchitectureTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="api_developer",
            password="apipassword123",
            years_of_experience=2
        )
        self.topic = Topic.objects.create(name="Tech")
        self.newspaper = Newspaper.objects.create(
            title="Tech Crunch Wroclaw",
            content="Python & Django backend infrastructure.",
            topic=self.topic
        )
        self.token_url = reverse("token_obtain_pair")
        self.newspaper_api_url = "/api/newspapers/"

    def test_jwt_token_generation(self):
        """Verify that the JWT authentication endpoint returns valid tokens"""
        data = {"username": "api_developer", "password": "apipassword123"}
        response = self.client.post(self.token_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_create_newspaper_via_api_authenticated(self):
        """
        Verify that authenticated users
        can successfully create records via REST API
        """
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "New Era of Backend",
            "content": "Comprehensive Docker & CI/CD guide.",
            "topic_id": self.topic.id,
            "publisher_ids": [self.user.id]
        }
        response = self.client.post(
            self.newspaper_api_url,
            data,
            format="json"
        )
        if response.status_code != status.HTTP_201_CREATED:
            self.fail(f"DRF Validation or Runtime Error: {response.data}")
        self.assertEqual(
            Newspaper.objects.filter(
                title="New Era of Backend"
            ).count(),
            1
        )

    def test_create_newspaper_api_anonymous_denied(self):
        """
        Verify that unauthenticated requests to create
        records are blocked
        """
        data = {
            "title": "Anon",
            "content": "Blocked",
            "topic_id": self.topic.id
        }
        response = self.client.post(
            self.newspaper_api_url,
            data,
            format="json"
        )
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED,
             status.HTTP_403_FORBIDDEN]
        )
