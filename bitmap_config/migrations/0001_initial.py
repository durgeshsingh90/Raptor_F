# Generated by Django 5.0.1 on 2024-02-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitmapConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subfield', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=10)),
                ('length_type', models.CharField(blank=True, max_length=10, null=True)),
                ('length', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
