from django.contrib import admin
from .models import Meseros1


# Register your models here.
@admin.register(Meseros1)
class Meseros1Admin(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad", "edad")