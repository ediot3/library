# Generated by Django 4.0.3 on 2022-03-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0004_remove_books_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='books',
            name='review',
            field=models.IntegerField(default=1),
        ),
    ]