# Generated by Django 5.0.7 on 2024-07-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0004_alter_student_attendance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
    ]
