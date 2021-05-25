# Generated by Django 3.2.3 on 2021-05-25 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_Number', models.CharField(max_length=255, unique=True, verbose_name='Roll_No')),
                ('name', models.CharField(max_length=225, verbose_name='name')),
                ('DOB', models.CharField(max_length=225, verbose_name='DOB')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(verbose_name='Mark')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devapp.detail')),
            ],
        ),
    ]