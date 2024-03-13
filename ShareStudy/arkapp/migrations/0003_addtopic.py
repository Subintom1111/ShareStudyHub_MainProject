# Generated by Django 5.0.2 on 2024-03-06 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arkapp', '0002_aptitudetestcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('total_questions', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('live_test', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arkapp.aptitudetestcourse')),
            ],
        ),
    ]
