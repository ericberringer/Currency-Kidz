from django.db import models

class QuizImages(models.Model):

    correct_answer = models.ImageField()
    incorrect_answer = models.ImageField()