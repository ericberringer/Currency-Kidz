from django.db import models

class WithdrawalEvent(models.Model):

    date = models.DateTimeField()
    name = models.CharField(max_length=50)
    saver = models.ForeignKey("Saver", on_delete=models.CASCADE)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10 ,decimal_places=2)
    sound_effect = models.URLField()