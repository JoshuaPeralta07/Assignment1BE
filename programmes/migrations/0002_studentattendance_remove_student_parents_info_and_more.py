# Generated by Django 5.0.7 on 2024-07-15 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='parents_info',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tuition_fee',
        ),
        migrations.AddField(
            model_name='student',
            name='attendance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programmes.studentattendance'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ParentInfo',
        ),
        migrations.DeleteModel(
            name='StudentTuitionFee',
        ),
    ]
