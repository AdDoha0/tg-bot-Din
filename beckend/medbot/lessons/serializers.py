from rest_framework import serializers
from .models import Volume, Lesson, Words





class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ("__all__",)


class LessonSerializer(serializers.ModelSerializer):
    words = WordsSerializer(many=True, read_only=True)  # Вложенный сериализатор для слов

    class Meta:
        model = Lesson
        fields = ("__all__",)


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("__all__",)


class VolumeSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)  # Вложенный сериализатор для уроков

    class Meta:
        model = Volume
        fields = ("__all__",)


class CreateVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ("__all__",)