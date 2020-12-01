from django.contrib import admin

# Register your models here.
from .models import Booking, Question, Choice, Conv

admin.site.register(Booking)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Conv)