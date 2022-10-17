# Generated by Django 4.1.2 on 2022-10-16 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_agent_trip_remove_client_client_commission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.agent'),
        ),
        migrations.AddField(
            model_name='trip',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]
