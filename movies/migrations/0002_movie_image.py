# Generated by Django 4.2.9 on 2024-05-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
