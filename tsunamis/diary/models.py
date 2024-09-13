from django.db import models

# надо сделать миграции


# Класс всех пловцов Цунамис в бд, что-то типо профиля
class Swimmer(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    category = models.CharField('Разряд', max_length=40)
    group = models.CharField('Группа', max_length=20)  # к примеру кракен, пираньи, медузы
    main_stroke = models.CharField('Основной стиль', max_length=20)
    second_stroke = models.CharField('Второй стиль', max_length=20, default='Нет')
    distances = models.CharField('Основные дистанции (м)', max_length=75)
    butterfly = models.CharField('50м батт', max_length=20, default='Неизвестно')
    backstroke = models.CharField('50м спина', max_length=20, default='Неизвестно')
    breaststroke = models.CharField('50м брасс', max_length=20, default='Неизвестно')
    freestyle = models.CharField('50м кроль', max_length=20, default='Неизвестно')

    password = models.CharField('Пароль', max_length=100)

    def __str__(self):
        return self.name, self.surname

    class Meta:
        verbose_name = 'Пловец'
        verbose_name_plural = 'Пловцы'


# Класс оценок в дневнике
class Mark(models.Model):
    swimmer = models.ForeignKey(Swimmer, on_delete=models.DO_NOTHING)
    mark = models.CharField('Оценка', max_length=2)
    date = models.DateField(auto_now_add=True, editable=True)