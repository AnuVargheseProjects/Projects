# Generated by Django 5.0.7 on 2024-09-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0002_remove_books_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='banner',
            field=models.ImageField(blank=True, default='books.jpg', upload_to=''),
        ),
    ]
