# Generated by Django 3.2.6 on 2021-08-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0005_alter_concert_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.CharField(default='Pavilion Theatre', max_length=100),
        ),
    ]
