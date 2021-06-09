from django.db import models

class Quiz(models.Model):

    name = models.CharField(max_length=50)
    quiz_image = models.ForeignKey("QuizImages", on_delete=models.CASCADE)
    saver = models.ForeignKey("Saver", on_delete=models.CASCADE)
