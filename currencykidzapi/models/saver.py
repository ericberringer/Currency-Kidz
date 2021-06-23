from django.db import models
from django.contrib.auth.models import User

class Saver(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image_url = models.ImageField()
    goal_amount = models.DecimalField(max_digits=10 ,decimal_places=2)
    created_on = models.DateTimeField()