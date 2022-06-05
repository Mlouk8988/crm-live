from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User, Question

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'gmail', 'message')

admin.site.register(Question, QuestionAdmin)
