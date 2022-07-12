from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NoteForm
from .models import Note

success_url = "/notes/"


class NoteCreateView(LoginRequiredMixin, CreateView):
    """Note create view to handle creating a new note"""

    model = Note
    form_class = NoteForm
    success_url = success_url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    """Note update view to handle updating a note"""

    model = Note
    form_class = NoteForm
    success_url = success_url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    """Note delete view to handle deleting a note"""

    model = Note
    success_url = success_url
    template_name = "notes/note_delete.html"


class NoteListView(LoginRequiredMixin, ListView):
    """Note list view to handle listing all notes"""

    model = Note
    template_name = "notes/list_notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        """Get the list of notes for this user"""
        return self.request.user.notes.all()  # type: ignore


class NoteDetailView(LoginRequiredMixin, DetailView):
    """Note detail view to handle showing a note"""

    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"
