# Generated by Django 5.0.3 on 2024-04-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_categories_car_price_car_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.CharField(choices=[('Tbilisi', 'Tbilisi'), ('Kutaisi', 'Kutaisi'), ('Batumi', 'Batumi'), ('Rustavi', 'Rustavi'), ('Poti', 'Poti'), ('Zugdidi', 'Zugdidi'), ('Gori', 'Gori'), ('Samtredia', 'Samtredia'), ('Khashuri', 'Khashuri'), ('Tsentraluri', 'Tsentraluri'), ('Telavi', 'Telavi'), ('Ozurgeti', 'Ozurgeti'), ('Sendaqi', 'Sendaqi'), ('Borjomi', 'Borjomi'), ('Akhalkalaki', 'Akhalkalaki'), ('Akhaltsikhe', 'Akhaltsikhe'), ('Kobuleti', 'Kobuleti'), ('Tkibuli', 'Tkibuli'), ('Martvili', 'Martvili'), ('Kaspi', 'Kaspi'), ('Tsqaltubo', 'Tsqaltubo'), ('Khulo', 'Khulo'), ('Chiatura', 'Chiatura'), ('Sagarejo', 'Sagarejo'), ('Lagodekhi', 'Lagodekhi'), ('Dusheti', 'Dusheti'), ('Sachkhere', 'Sachkhere'), ('Kareli', 'Kareli'), ('Abasha', 'Abasha')], default='Tbilisi', max_length=40),
        ),
    ]
