# Generated by Django 3.2.4 on 2021-07-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='go_to_school_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Nữ'), (1, 'Nam')]),
        ),
    ]
