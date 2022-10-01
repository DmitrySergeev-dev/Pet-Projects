from django.db import models


class Human(models.Model): #Базовый класс
    full_name = models.CharField(max_length=255, verbose_name='ФИО')

    class Meta:
        abstract = True


class Student(Human):
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(Human):
    academic_degree = models.CharField(max_length=255, verbose_name='Ученая степень')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватель'


class Subject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет обучения'
        verbose_name_plural = 'Предметы обучения'


class StudentsGroup(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа обучаемых'
        verbose_name_plural = 'Группы обучаемых'


class Lesson(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет обучения')
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, verbose_name='Преподаватель')
    students_group = models.ForeignKey('StudentsGroup', on_delete=models.PROTECT, verbose_name='Группы обучаемых')
    date_time = models.DateTimeField(verbose_name='Дата проведения')
    is_finished = models.BooleanField(default=False, verbose_name='Состояние занятия', help_text='Поставьте галочку, '
                                                                                                 'если занятие '
                                                                                                 'завершено')
    absent_students = models.ManyToManyField(Student, verbose_name='Отсутствующие студенты',help_text='Выделите с '
                                                                                                      'помощью клавиш Ctrl или Shift студентов из списка')

    def __str__(self):
        return f'{self.subject}, {self.date_time.strftime("%m/%d/%Y, %H:%M:%S")}'

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
# Create your models here.
