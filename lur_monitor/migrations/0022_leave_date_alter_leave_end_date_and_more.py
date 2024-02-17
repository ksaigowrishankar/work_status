# Generated by Django 4.2.5 on 2023-12-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0021_leave_type_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='start_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
