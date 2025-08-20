from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=512, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["is_done", "-created_at"]

    def __str__(self):
        return f"{self.content[:30]} - {self.created_at}"
