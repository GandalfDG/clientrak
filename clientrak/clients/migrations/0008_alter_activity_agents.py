# Generated by Django 4.1.3 on 2022-11-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_activity_options_alter_activity_agents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='agents',
            field=models.ManyToManyField(blank=True, related_name='activities', to='clients.agent'),
        ),
    ]