# Generated by Django 3.2.6 on 2021-08-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0003_concert_doors'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='guests',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
