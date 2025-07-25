# Generated by Django 5.2.4 on 2025-07-21 07:05

import django.db.models.deletion
import file_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fetenaArchive', '0005_remove_user_name_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=file_api.utils.exam_file_path)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_file', to='fetenaArchive.exam')),
            ],
        ),
    ]
