# Generated by Django 4.2.6 on 2024-03-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rodon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
