# Generated by Django 4.1.7 on 2023-02-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_leaser_address_leaser_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaser',
            name='phone',
            field=models.CharField(default=True, max_length=15, verbose_name='Телефон'),
        ),
    ]
