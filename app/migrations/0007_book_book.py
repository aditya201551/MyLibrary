# Generated by Django 3.2.3 on 2021-06-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210606_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.FileField(default='test', upload_to='books/'),
            preserve_default=False,
        ),
    ]