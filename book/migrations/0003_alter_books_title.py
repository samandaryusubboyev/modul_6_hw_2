# Generated by Django 5.0.6 on 2024-06-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_books_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
