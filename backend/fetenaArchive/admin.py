from django.contrib import admin
from .models import Exam, User, DifficultyRating
# Register your models here.



admin.site.register(Exam)
admin.site.register(User)
admin.site.register(DifficultyRating)