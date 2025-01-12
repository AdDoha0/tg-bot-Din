from django.db import models


class Volume(models.Model):
    '''Модель томов, related_name связь с Lesson'''
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Том'
        verbose_name_plural = 'Тома'


class Lesson(models.Model):
    '''Модель урока, cвязи с моделями Volume и related_name связь с Words'''
    title = models.CharField(max_length=200)
    summary = models.TextField()
    created_ar = models.DateTimeField(auto_now_add=True)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='lessons')  # Связь с томом
    video_url = models.URLField(blank=True, null=True)  # Ссылка на видео


    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


    def __str__(self):
        return self.title


class Words(models.Model):
    '''Модель слова, связи с моделями Lesson и related_name связь с Lesson'''
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='words')  # Связь с уроком
    term = models.CharField(max_length=100)  # Само слово
    definition = models.TextField()  # Определение или перевод слова

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return f"{self.term} ({self.lesson.title})"






