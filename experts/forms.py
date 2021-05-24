from django import forms

from experts.models import ExpertProfile


class ExpertCreateForm(forms.ModelForm):
    class Meta:
        model = ExpertProfile
        exclude = ['user', 'schedule', 'is_verified']
