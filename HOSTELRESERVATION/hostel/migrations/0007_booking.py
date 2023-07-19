# Generated by Django 4.2.3 on 2023-07-16 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostel', '0006_alter_hostel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel')),
                ('hostel_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.hostelowner')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
