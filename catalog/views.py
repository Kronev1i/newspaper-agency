from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    RedactorCreationForm,
    NewspaperCreationForm,
    TopicNameSearchForm,
    NewspaperTitleSearchForm,
    RedactorUsernameSearchForm
)
from .models import Redactor, Newspaper, Topic

@login_required
def toggle_assign_to_newspaper(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    if request.user in newspaper.publishers.all():
        newspaper.publishers.remove(request.user)
    else:
        newspaper.publishers.add(request.user)
    return redirect("catalog:newspaper-detail", pk=pk)


@login_required
def index(request):
    """View function for the home page of the site."""
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(
        request,
        "newspaper/index.html",
        context=context
    )


class TopicListView(
    LoginRequiredMixin,
    generic.ListView
):
    """View class for the list of topics with search functionality."""
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    paginate_by = 5

    def get_context_data(
        self,
        *,
        object_list=...,
        **kwargs
    ):
        """Pass search form to the template context."""
        context = super(
            TopicListView,
            self
        ).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicNameSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        """Filter topics by name search query."""
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TopicDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    """Detailed information about a specific topic."""
    template_name = "newspaper/topic_detail.html"
    model = Topic


class TopicCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("catalog:topic-list")


class TopicUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("catalog:topic-list")


class TopicDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Topic
    template_name = "newspaper/topic_confirm_delete.html"
    success_url = reverse_lazy("catalog:topic-list")


class NewspaperListView(
    LoginRequiredMixin,
    generic.ListView
):
    """View class for the list of newspapers with optimized topic loading."""
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 5
    queryset = Newspaper.objects.all().select_related("topic")

    def get_context_data(
        self,
        *,
        object_list=...,
        **kwargs
    ):
        """Include NewspaperTitleSearchForm in the context."""
        context = super(
            NewspaperListView,
            self
        ).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperTitleSearchForm(
            initial={
                "title": title
            }
        )
        return context

    def get_queryset(self):
        """Filter newspapers by title."""
        queryset = super().get_queryset()
        title = self.request.GET.get("title")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset


class NewspaperCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Newspaper
    form_class = NewspaperCreationForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("catalog:newspaper-list")


class NewspaperUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Newspaper
    form_class = NewspaperCreationForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("catalog:newspaper-list")


class NewspaperDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Newspaper
    template_name = "newspaper/newspaper_confirm_delete.html"
    success_url = reverse_lazy("catalog:newspaper-list")


class NewspaperDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    template_name = "newspaper/newspaper_detail.html"
    model = Newspaper


class RedactorListView(
    LoginRequiredMixin,
    generic.ListView
):
    """View class for the list of redactors with username search."""
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    paginate_by = 5

    def get_context_data(
        self, *, object_list=..., **kwargs
    ):
        """Pass RedactorUsernameSearchForm to the template."""
        context = super(
            RedactorListView,
            self
        ).get_context_data(**kwargs)
        username = self.request.GET.get("name", "")
        context["search_form"] = RedactorUsernameSearchForm(
            initial={
                "username": username
            }
        )
        return context

    def get_queryset(self):
        """Filter redactors by username."""
        queryset = super().get_queryset()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class RedactorCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Redactor
    template_name = "newspaper/redactor_form.html"
    form_class = RedactorCreationForm
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Redactor
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "years_of_experience"
    )
    template_name = "newspaper/redactor_form.html"
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Redactor
    template_name = "newspaper/redactor_confirm_delete.html"
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    """Detailed information about a redactor with their newspapers."""
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


def logout_confirm_view(request):
    return render(request, "registration/logout_confirm.html")
