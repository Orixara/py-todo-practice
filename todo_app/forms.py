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


class TaskSearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by content or tags"}
        )
    )