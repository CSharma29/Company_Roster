# Generated by Django 3.2.2 on 2021-05-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='selected_students',
            field=models.TextField(blank=True, null=True),
        ),
    ]