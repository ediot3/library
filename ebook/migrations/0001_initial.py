# Generated by Django 4.0.3 on 2022-03-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=200)),
                ('catagory', models.CharField(max_length=200)),
            ],
        ),
    ]
