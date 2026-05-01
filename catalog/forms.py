from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class NewspaperCreationForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorUsernameSearchForm(forms.Form):
    username = forms.CharField(max_length=255, required=False)


class NewspaperTitleSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)


class TopicNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)


class RedactorExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["years_of_experience"]

    def clean_years_of_experience(self):
        years = self.cleaned_data["years_of_experience"]
        if not (0 <= years <= 70):
            raise ValidationError("Experience should be between 0 and 70 years.")
        return years
