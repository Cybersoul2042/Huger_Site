# Generated by Django 5.0.7 on 2024-07-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='amir', max_length=128),
            preserve_default=False,
        ),
    ]
