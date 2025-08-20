from django import forms

from todo_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "datetime-local",
            }
        )
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
