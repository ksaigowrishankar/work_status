# Generated by Django 4.2.5 on 2023-12-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0017_employee_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='app_img',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]