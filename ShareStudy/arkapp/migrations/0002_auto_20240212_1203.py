# Generated by Django 3.0.5 on 2024-02-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arkapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='prepare_exam',
            name='end_time',
        ),
    ]