# Generated by Django 5.0.6 on 2024-06-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/book_images/'),
        ),
    ]
