# Generated by Django 4.0 on 2022-01-19 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]