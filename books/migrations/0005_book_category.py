# Generated by Django 4.0.1 on 2022-08-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_comment_connect_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
