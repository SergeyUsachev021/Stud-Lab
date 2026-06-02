from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

def validate_course(value):
    if (value > 6) or (value < 1): raise ValidationError("Курс может быть 1-6")

class Lab(models.Model):
    class LevelType(models.TextChoices):
        BACHELOR = 'bachelor', 'Бакалавриат'
        SPECIALIST = 'specialist', 'Специалитет'
        MASTER = 'master', 'Магистратура'
        POSTGRADUATE = 'postgraduate', 'Аспирантура'

    class WorkType(models.TextChoices):
        LABORATORY = 'laboratory', 'Лабораторная'
        ESSAY = 'essay', 'Реферат'
        COURSEWORK = 'coursework', 'Курсовая'
        DIPLOMA = 'diploma', 'ВКР'

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(choices=LevelType, max_length=15)
    course = models.IntegerField(validators=[validate_course])
    year = models.CharField(max_length=4)
    university = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)
    type_work = models.CharField(choices=WorkType, max_length=15)
    author = models.CharField(max_length=200, blank=True, null=True)
    manager = models.CharField(max_length=200, blank=True, null=True)
    downloaded_times = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

class LabFile(models.Model):
    lab = models.ForeignKey(Lab, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='lab_files/')

    def __str__(self):
        return self.file.name

class ArchivedLab(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='archived_labs',
    )
    lab = models.ForeignKey(
        Lab,
        on_delete=models.CASCADE,
        related_name='archive_items',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'lab'],
                name='unique_archived_lab_per_user',
            ),
        ]
        verbose_name = 'Лабораторная в архиве'
        verbose_name_plural = 'Архив лабораторных'

    def __str__(self):
        return f'{self.user}: {self.lab}'