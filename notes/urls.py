from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.NoteListView.as_view(),
        name="list_notes",
    ),
    path(
        "<int:pk>/",
        views.NoteDetailView.as_view(),
        name="note_detail",
    ),
    path(
        "<int:pk>/edit",
        views.NoteUpdateView.as_view(),
        name="note_update",
    ),
    path(
        "<int:pk>/delete",
        views.NoteDeleteView.as_view(),
        name="note_delete",
    ),
    path(
        "new/",
        views.NoteCreateView.as_view(),
        name="note_new",
    ),
]
