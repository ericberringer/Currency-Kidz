from django.db import models

class Currency (moedels.Model):

    quarter = models.IntegerField()
    dime = models.IntegerField()
    nickel = models.IntegerField()
    penny = models.IntegerField()
    one_dollar = models.IntegerField()
    five_dollars = models.IntegerField()
    ten_dollars = models.IntegerField()
    twenty_dollars = models.IntegerField()
    fifty_dollars = models.IntegerField()
    one_hundred_dollars = models.IntegerField()