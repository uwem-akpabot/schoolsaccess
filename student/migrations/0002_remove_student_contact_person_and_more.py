# Generated by Django 4.1.7 on 2023-06-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='student',
            name='contact_person_phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AddField(
            model_name='student',
            name='parent1',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent1_phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='parent2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent2_phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]