# Generated by Django 3.2.4 on 2021-07-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencykidzapi', '0006_alter_saver_goal_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saver',
            name='goal_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
