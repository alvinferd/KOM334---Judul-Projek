# Generated by Django 3.2.4 on 2021-06-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210614_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alatlab',
            name='gambarAlat',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads/alat/'),
        ),
    ]
