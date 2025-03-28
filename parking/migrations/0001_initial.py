# Generated by Django 5.1.7 on 2025-03-17 20:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valid_from', models.DateTimeField()),
                ('valid_until', models.DateTimeField()),
                ('usage_count', models.PositiveIntegerField(default=0)),
                ('max_usage_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyCommunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('total_capacity', models.PositiveIntegerField()),
                ('available_capacity', models.PositiveIntegerField()),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
                ('no_of_floors', models.CharField(default=1, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.CharField(max_length=20)),
                ('is_occupied', models.BooleanField(default=False)),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('Subscription_Type', models.CharField(default='Regular', max_length=20)),
                ('license_id', models.PositiveIntegerField(default=False, unique=True)),
                ('Wallet_Balance', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('Registration_Date', models.DateTimeField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Faulty', 'Faulty')], default='Active', max_length=20)),
                ('last_maintenance', models.DateTimeField(blank=True, null=True)),
                ('last_check', models.DateTimeField(auto_now=True)),
                ('parking_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_slots', models.PositiveIntegerField()),
                ('available_slots', models.PositiveIntegerField()),
                ('zone_type', models.CharField(choices=[('Regular', 'Regular'), ('VIP', 'VIP')], max_length=50)),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_zones', to='parking.garage')),
            ],
        ),
        migrations.AddField(
            model_name='parkingslot',
            name='parking_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_slots', to='parking.parkingzone'),
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('Car', 'Car'), ('Bike', 'Bike'), ('Truck', 'Truck')], max_length=20)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weekly_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('parking_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingzone')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(default='Reserved', max_length=20)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking.familycommunity')),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_time', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Pending', max_length=20)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking.familycommunity')),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parking.reservation')),
                ('payer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking.user')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('subscription_type', models.CharField(choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('parking_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingzone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.user')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlotReservationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_start', models.DateTimeField()),
                ('reservation_end', models.DateTimeField()),
                ('status', models.CharField(choices=[('Reserved', 'Reserved'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], max_length=20)),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
                ('reserved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.user')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('Reservation Reminder', 'Reservation Reminder'), ('Payment Reminder', 'Payment Reminder'), ('General Alert', 'General Alert')], max_length=100)),
                ('message', models.TextField()),
                ('notification_time', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.user')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Member', 'Member')], default='Member', max_length=20)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='parking.familycommunity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.user')),
            ],
        ),
        migrations.AddField(
            model_name='familycommunity',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_creator', to='parking.user'),
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('rating', models.PositiveIntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parking_slot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking.parkingslot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.user')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=15, unique=True)),
                ('vehicle_type', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(default=False, max_length=20)),
                ('vehicle_color', models.CharField(default=False, max_length=20)),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.user')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.vehicle'),
        ),
        migrations.AddField(
            model_name='parkingslot',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking.vehicle'),
        ),
        migrations.CreateModel(
            name='ParkingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
                ('parking_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingzone')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('event_type', models.CharField(choices=[('Parked', 'Parked'), ('Exited', 'Exited')], default='Parked', max_length=20)),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=255)),
                ('resolved', models.BooleanField(default=False)),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.vehicle')),
            ],
        ),
    ]
