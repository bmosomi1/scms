# Generated by Django 2.2.13 on 2020-12-22 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_student_temporary_id'),
        ('academics', '0010_auto_20201219_0025'),
        ('result', '0008_subjectgroup_subjects'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'semester', 'subject')},
        ),
    ]