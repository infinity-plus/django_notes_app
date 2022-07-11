from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/list_notes.html"
    context_object_name = "notes"


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"
