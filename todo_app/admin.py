from django.contrib import admin

from todo_app.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "is_done", "created_at", "deadline"]
    list_filter = ["is_done", "created_at", "tags"]
    search_fields = ["content"]
    list_editable = ["is_done"]
    filter_horizontal = ["tags"]
