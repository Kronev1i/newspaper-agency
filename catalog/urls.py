from django.contrib.auth.views import (
    LogoutView,
    LoginView,
)
from django.urls import path

from .views import (
    index,
    TopicListView,
    NewspaperListView,
    RedactorListView,
    NewspaperDetailView,
    RedactorDetailView, logout_confirm_view,
)

urlpatterns = [
    path(
        "", index,
        name="index"
    ),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "confirm-logout/",
        logout_confirm_view,
        name="logout-confirm-view"
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login"
    )
]


app_name = "catalog"
