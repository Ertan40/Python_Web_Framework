# Generated by Django 4.2.2 on 2023-07-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
