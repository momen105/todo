from django import forms
from .models import TodoWork


class TodoWorkForm(forms.ModelForm):
    class Meta:
        model = TodoWork
        # fields = ["title", "des", "note"]
        fields = "__all__"
