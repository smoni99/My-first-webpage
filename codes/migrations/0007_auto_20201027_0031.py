# Generated by Django 3.1.2 on 2020-10-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0006_auto_20201026_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='content',
        ),
        migrations.AlterField(
            model_name='code',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]