from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 7
    queryset = Task.objects.prefetch_related("tags").order_by(
        "is_done", "-created_at"
    )


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.order_by("name")
