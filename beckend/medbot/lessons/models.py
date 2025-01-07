from django.db import models


class Volume(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    created_ar = models.DateTimeField(auto_now_add=True)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='lessons')  # Связь с томом
    video_url = models.URLField(blank=True, null=True)  # Ссылка на видео

    def __str__(self):
        return self.title


class Words(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='words')  # Связь с уроком
    term = models.CharField(max_length=100)  # Само слово
    definition = models.TextField()  # Определение или перевод слова




