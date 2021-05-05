# Generated by Django 3.2.1 on 2021-05-05 11:54

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
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=200, null=True)),
                ('cinema_screens', models.IntegerField(default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200, null=True)),
                ('city_state', models.CharField(max_length=200, null=True)),
                ('city_pin_code', models.IntegerField(default=0, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=200, null=True)),
                ('screen_seats', models.IntegerField(default=0)),
                ('cinema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search_movie.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10, null=True)),
                ('seat_type', models.BooleanField(default=False, null=True)),
                ('screen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search_movie.screen')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_password', models.CharField(max_length=200, null=True)),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('user_phone', models.IntegerField(default=0, max_length=10)),
                ('user_email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search_movie.city'),
        ),
    ]
