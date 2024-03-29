# Generated by Django 5.0.2 on 2024-03-11 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arkapp', '0003_addtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arkapp.aptitudetestcourse')),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arkapp.addtopic')),
            ],
        ),
    ]
