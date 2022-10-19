# Generated by Django 4.1.1 on 2022-10-19 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_branch_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.recipe'),
        ),
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.recipe'),
        ),
    ]
