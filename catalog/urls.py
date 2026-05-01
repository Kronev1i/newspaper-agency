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
    RedactorDetailView, logout_confirm_view, NewspaperCreateView, TopicCreateView, RedactorCreateView,
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
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
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
