# Generated by Django 5.0.9 on 2024-09-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
