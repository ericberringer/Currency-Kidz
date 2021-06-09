# Generated by Django 3.2.4 on 2021-06-09 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencykidzapi', '0002_auto_20210609_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.ImageField(upload_to='')),
                ('incorrect_answer', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quiz_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencykidzapi.quizimages')),
                ('saver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencykidzapi.saver')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencykidzapi.quiz')),
            ],
        ),
    ]
