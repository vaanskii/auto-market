# Generated by Django 5.0.3 on 2024-04-21 06:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(choices=[('Acura', 'Acura'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Audi', 'Audi'), ('Bentley', 'Bentley'), ('BMW', 'BMW'), ('Bugatti', 'Bugatti'), ('Buick', 'Buick'), ('Cadillac', 'Cadillac'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Citroën', 'Citroën'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Genesis', 'Genesis'), ('GMC', 'GMC'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lamborghini', 'Lamborghini'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Lincoln', 'Lincoln'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mercedes-Benz', 'Mercedes-Benz'), ('MINI', 'MINI'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('RAM', 'RAM'), ('Rolls-Royce', 'Rolls-Royce'), ('Saab', 'Saab'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], max_length=100)),
            ],
        ),
    ]
