from django.contrib import admin

from . import models


class NoteAdmin(admin.ModelAdmin):
    """Note admin to handle notes"""

    list_display = ("title",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = (
        "-created_at",
        "-updated_at",
    )


admin.site.register(models.Note, NoteAdmin)
