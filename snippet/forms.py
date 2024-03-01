from django import forms
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['original_content', 'key']


class DecryptForm(forms.Form):
    key = forms.CharField(max_length=255, required=True)
