# Generated by Django 3.2.8 on 2022-12-24 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='ticket_type',
        ),
        migrations.DeleteModel(
            name='TicketType',
        ),
    ]