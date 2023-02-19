# Generated by Django 4.1.7 on 2023-02-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_hcstype_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='lease_end',
        ),
        migrations.RemoveField(
            model_name='building',
            name='lease_start',
        ),
        migrations.AddField(
            model_name='building',
            name='name_build',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='pointer',
            field=models.IntegerField(null=True, verbose_name='Номер'),
        ),
    ]