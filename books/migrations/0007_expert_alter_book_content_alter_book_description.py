# Generated by Django 4.0.1 on 2022-08-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_category_alter_book_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='expert_images/')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='content',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=2500),
        ),
    ]