# Generated by Django 4.1.3 on 2022-11-19 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_activity_create_date_activity_updated_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='time_spent',
        ),
        migrations.AlterField(
            model_name='activity',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='clients.trip'),
        ),
    ]
