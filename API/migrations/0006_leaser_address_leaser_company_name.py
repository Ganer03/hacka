# Generated by Django 4.1.7 on 2023-02-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_commercialobject_photo_com_obj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaser',
            name='address',
            field=models.CharField(default='г.Москва ул.Кутузова, 119', max_length=120, verbose_name='Юр.адрес'),
        ),
        migrations.AddField(
            model_name='leaser',
            name='company_name',
            field=models.CharField(default='ООО СтройИнвест', max_length=60, verbose_name='Название юр.лица'),
        ),
    ]
