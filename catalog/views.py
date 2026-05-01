from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import RedactorCreationForm, NewspaperCreationForm
from .models import Redactor, Newspaper, Topic

@login_required
def index(request):
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
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    paginate_by = 5


class TopicCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("catalog:topic-list")


class NewspaperListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 5
    queryset = Newspaper.objects.all().select_related("topic")


class NewspaperCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Newspaper
    form_class = NewspaperCreationForm
    template_name = "newspaper/newspaper_form.html"
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
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    paginate_by = 5


class RedactorCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Redactor
    template_name = "newspaper/newspaper_form.html"
    form_class = RedactorCreationForm
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


def logout_confirm_view(request):
    return render(request, "registration/logout_confirm.html")
