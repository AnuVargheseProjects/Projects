# Generated by Django 5.0.7 on 2024-09-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0003_books_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='banner',
            field=models.ImageField(blank=True, default='books.jpg', null=True, upload_to='images/'),
        ),
    ]
