# Generated by Django 3.0.7 on 2021-07-12 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210711_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.RemoveField(
            model_name='like',
            name='is_like',
        ),
    ]
