# Generated by Django 3.2.15 on 2022-09-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='manzil',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
