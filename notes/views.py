from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NoteForm


from .models import Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = "/notes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = "/notes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = "/notes/"
    template_name = "notes/note_delete.html"


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/list_notes.html"
    context_object_name = "notes"


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"
