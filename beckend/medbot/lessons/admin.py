from django.contrib import admin

from .models import *



@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume', 'created_ar', 'video_url')
    list_filter = ('volume', 'created_ar')
    search_fields = ('title', 'summary')

@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ('term', 'lesson', 'definition')
    list_filter = ('lesson',)
    search_fields = ('term', 'definition')
