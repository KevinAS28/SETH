# Generated by Django 3.1.7 on 2021-03-21 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETH', '0002_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='formatted_address',
            field=models.CharField(default='Gadjah Mada University', max_length=200),
        ),
    ]
