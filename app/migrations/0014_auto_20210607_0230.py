# Generated by Django 3.2 on 2021-06-06 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_book_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(upload_to='books'),
        ),
    ]