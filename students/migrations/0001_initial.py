# Generated by Django 5.1.7 on 2025-03-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
    ]
