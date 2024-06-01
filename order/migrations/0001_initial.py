# Generated by Django 4.2.7 on 2024-05-31 23:17

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('O', 'Ongoing'), ('C', 'Completed')], default='P', max_length=1)),
                ('post_content', models.TextField()),
                ('departure_address', models.CharField(max_length=100)),
                ('arrival_address', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(choices=[('M', 'Motorcycle'), ('C', 'Car')], max_length=1)),
                ('weight_limit', models.FloatField()),
                ('payment_method', models.CharField(choices=[('CC', 'Credit Card'), ('CS', 'Cash')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]