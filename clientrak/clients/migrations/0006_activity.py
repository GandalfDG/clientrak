# Generated by Django 4.1.3 on 2022-11-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_remove_agent_first_name_remove_agent_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('agents', models.ManyToManyField(to='clients.agent')),
            ],
        ),
    ]