from django.views import generic

from todo_app.models import Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 7
    queryset = Task.objects.prefetch_related("tags").order_by("is_done", "-created_at")
