# Generated by Django 3.0.2 on 2022-03-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
