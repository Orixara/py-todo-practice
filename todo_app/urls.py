from django.urls import path

from todo_app.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
]


app_name = "todo"
