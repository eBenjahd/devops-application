from django.db import models
from django.contrib.auth.models import User


class Doubt(models.Model):
    class Mode(models.TextChoices):
        CONSULTOR = "consultor", "Consultor"
        ERROR = "error", "Diagnosticar error"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consultas", null=True, blank=True,)
    mode = models.CharField(max_length=20, choices=Mode.choices)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]