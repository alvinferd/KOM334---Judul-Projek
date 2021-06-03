# Generated by Django 3.2.2 on 2021-06-03 02:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210602_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_Submisi',
            fields=[
                ('id_form', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ruangan', models.CharField(max_length=100)),
                ('date_form', models.DateField()),
                ('file1', models.FileField(upload_to='uploads/')),
                ('file2', models.FileField(upload_to='uploads/')),
                ('Verifikasi', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorium',
            fields=[
                ('id_labor', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ruangan', models.CharField(max_length=100)),
                ('departemen', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PeminjamanRuangan',
            fields=[
                ('id_peminjaman', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_peminjaman', models.DateField()),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.form_submisi')),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.laboratorium')),
                ('peminjam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mahasiswa')),
            ],
        ),
        migrations.AddField(
            model_name='form_submisi',
            name='ruangan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.laboratorium'),
        ),
        migrations.AddField(
            model_name='form_submisi',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mahasiswa'),
        ),
        migrations.AddField(
            model_name='alatlab',
            name='lab_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.laboratorium'),
        ),
    ]
