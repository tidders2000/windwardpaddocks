# Generated by Django 4.1.1 on 2022-10-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_extra_horse_alter_booking_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='extra_horse',
            field=models.BooleanField(null=True),
        ),
    ]
