# Generated by Django 3.1.2 on 2020-10-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0004_auto_20201026_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='content',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]