from django import forms
from django.forms import ModelForm, ValidationError
from .models import Note


class NoteForm(ModelForm):
    """Note form"""

    class Meta:
        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control my-5"}),
            "content": forms.Textarea(attrs={"class": "form-control mb-5"}),
        }
        labels = {
            "title": "Note Title: ",
            "content": "Take a note:",
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "django" not in title.lower():
            raise ValidationError("Notes should have django in title!")
        return title
