from django.db import models

class Currency (models.Model):

    quarter = models.DecimalField(max_digits=3, decimal_places=2)
    dime = models.DecimalField(max_digits=3, decimal_places=2)
    nickel = models.DecimalField(max_digits=3, decimal_places=2)
    penny = models.DecimalField(max_digits=3, decimal_places=2)
    one_dollar = models.IntegerField()
    five_dollars = models.IntegerField()
    ten_dollars = models.IntegerField()
    twenty_dollars = models.IntegerField()
    fifty_dollars = models.IntegerField()
    one_hundred_dollars = models.IntegerField()