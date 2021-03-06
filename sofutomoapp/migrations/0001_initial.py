# Generated by Django 3.2.6 on 2021-08-28 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('good_counts', models.IntegerField(blank=True, default=0, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(max_length=240)),
                ('member', models.IntegerField(blank=True, default=0, null=True)),
                ('match_date', models.DateField(blank=True, null=True)),
                ('match_time', models.TimeField(blank=True, null=True)),
                ('URL', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(max_length=240)),
                ('URL', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
