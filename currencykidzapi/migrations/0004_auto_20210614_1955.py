# Generated by Django 3.2.4 on 2021-06-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencykidzapi', '0003_question_quiz_quizimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositevent',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='withdrawalevent',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
