from django.contrib import admin
from .models import Saver, Currency, DepositEvent, WithdrawalEvent, Question, Quiz, QuizImages

# Register your models here.
admin.site.register(Saver)
admin.site.register(Currency)
admin.site.register(DepositEvent)
admin.site.register(WithdrawalEvent)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizImages)