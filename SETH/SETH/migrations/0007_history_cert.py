# Generated by Django 3.1.7 on 2021-03-21 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SETH', '0006_place_supported_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='cert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_history', to='SETH.certificate'),
        ),
    ]