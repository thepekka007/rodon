# Generated by Django 4.2.6 on 2024-03-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('subject', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
