from django.db import models

class DepositEvent(models.Model):

    date = models.DateTimeField()
    name = models.CharField(max_length=50)
    saver = models.ForeignKey("Saver", on_delete=models.CASCADE)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)
    total = models.IntegerField()
    sound_effect = models.URLField()