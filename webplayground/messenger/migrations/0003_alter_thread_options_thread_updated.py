# Generated by Django 5.0.7 on 2024-10-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_message_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
