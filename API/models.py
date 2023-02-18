from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime
from django.utils.timezone import localdate


class TimeMixin(models.Model):
    update_time = models.DateTimeField('Последнее обновление', auto_now=True)
    creation_time = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        abstract = True


# Человек
class User(TimeMixin):
    name = models.CharField(verbose_name="Имя", max_length=60)
    surname = models.CharField(verbose_name="Фамилия", max_length=60)
    patronymic = models.CharField(verbose_name="Отчество", max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}"

    class Meta:
        abstract = True


class Transfer(TimeMixin):
    price = models.IntegerField(verbose_name="Сумма платежа")


# Арендодатель
class Landlord(User):
    password = models.CharField(verbose_name="Пароль", max_length=60)

    def get_buildings(self):
        return Building.objects.filter(landlord=self).values()

    def get_commercial_objects(self):
        return CommercialObject.objects.filter(building__landlord=self).values()

    def expense(self):
        y = sum([x.expenses() for x in Building.objects.filter(landlord=self).all()])
        return y

    def incomer(self):
        return sum(x.income() for x in Building.objects.filter(landlord=self).all())

# Арендатор
class Leaser(User):
    transfers = models.ManyToManyField(Transfer, blank=True)
    password = models.CharField(verbose_name="Пароль", max_length=60)

    def get_commercial_objects(self):
        return CommercialObject.objects.filter(leaser=self).values()


# Должность
class Position(TimeMixin):
    position_name = models.CharField(verbose_name="", max_length=40)
    salary = models.IntegerField(verbose_name="Зарплата")

    def __str__(self):
        return self.position_name


class Personal(User):
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Должность')
    phone = models.CharField(verbose_name='Телефон', max_length=15)

    def get_pos_name(self):
        return str(self.position)

    def get_salary(self):
        return self.position.salary;


# Траты на обслуживание
class Service(TimeMixin):
    price = models.IntegerField(verbose_name="")
    name = models.CharField(verbose_name="", max_length=40)
    description = models.TextField(verbose_name="")


# Строения
class Building(TimeMixin):
    name_build = models.CharField(verbose_name='Имя', max_length=40, null=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=80)
    personal = models.ManyToManyField(Personal, blank=True)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.address

    def get_services(self):
        result = []
        for service in self.services.values():
            result.append(service)

        return result

    def get_personal(self):
        result = {}
        result_pos = {}
        for person in self.personal.values():
            position = result.setdefault(person.get('position_id', 1), [])
            position.append(person)

        for key, value in result.items():
            pers_type = Position.objects.get(pk=key)
            key = str(pers_type)
            result_pos[key] = {
                "salary": pers_type.salary,
                "personal": value
            }

        return result_pos

    def income(self):
        return sum([x.income() for x in CommercialObject.objects.filter(building=self)])

    def expenses(self):
        return sum([x.price for x in self.services.all()])+sum([x.position.salary for x in self.personal.all()])


# Тип ЖКХ
class HcsType(TimeMixin):
    name = models.CharField(verbose_name="", max_length=40)
    price = models.FloatField(verbose_name="", default=5)

    def __str__(self):
        return self.name


# ЖКХ
class Hcs(TimeMixin):
    hcs_type = models.ForeignKey(HcsType, verbose_name="Тип ЖКХ", on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name="Значение")
    author = models.ForeignKey(Leaser, verbose_name="Автор", on_delete=models.SET_NULL, null=True)

    def price(self):
        hcs = Hcs.objects.filter(author=self.author, hcs_type=self.hcs_type, pk__lt=self.pk).order_by("-pk").first()
        return (self.value - hcs.value) * self.hcs_type.price

    def __str__(self):
        return str(self.hcs_type)


# Помещения
class CommercialObject(TimeMixin):
    pointer = models.IntegerField(verbose_name="Номер", null=True)
    building = models.ForeignKey(Building, verbose_name="Строения", on_delete=models.CASCADE)
    leaser = models.ForeignKey(Leaser, verbose_name="Арендатор", on_delete=models.SET_NULL, null=True,
                               blank=True)
    rent_price = models.IntegerField(verbose_name="Стоимость аренды")
    square = models.FloatField(verbose_name="Площадь")
    description = models.TextField(verbose_name="Описание")
    document = models.FileField(verbose_name="Договор аренды", upload_to="documents", blank=True)

    def income(self):
        return self.rent_price if bool(self.leaser) else 0

    def leaser_name(self):
        return str(self.leaser)

    def building_address(self):
        return str(self.building)

    def get_hcs(self):
        hgs_types = {}
        hgs_types_id = {}
        for item in Hcs.objects.filter(author=self.leaser).order_by("-pk").values():
            hgs_type = item.get('hcs_type_id', 1)
            hgs = hgs_types_id.setdefault(hgs_type, [])
            if len(hgs) < 12:
                hgs.append(item)

        for key, value in hgs_types_id.items():
            key = str(HcsType.objects.get(pk=key))
            hgs_types[key] = value

        return hgs_types

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
