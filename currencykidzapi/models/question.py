from django.db import models

class Question(models.Model):

    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE)