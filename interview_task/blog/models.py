from django.db import models
from django.contrib.auth.models import User

from django_prometheus.models import ExportModelOperationsMixin

SCORE_CHOICES = [(i, i) for i in range(6)]


class Post(ExportModelOperationsMixin('Post'), models.Model):
    author = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    meadPostScore = models.DecimalField(
        max_digits=3, decimal_places=2, default=0)
    countOfUsers = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'


class Score(ExportModelOperationsMixin('Score'),models.Model):
    user = models.ForeignKey(
        User, related_name="viewer", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="scores", on_delete=models.CASCADE)
    value = models.PositiveIntegerField(choices=SCORE_CHOICES, default=0)
    scoredAt = models.DateTimeField(auto_now_add=True)
