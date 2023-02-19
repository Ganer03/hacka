# Generated by Django 4.1.7 on 2023-02-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_building_photo_build'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialobject',
            name='photo_com_obj',
            field=models.FileField(null=True, upload_to='buildings', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='building',
            name='photo_build',
            field=models.FileField(null=True, upload_to='buildings', verbose_name='photo'),
        ),
    ]
