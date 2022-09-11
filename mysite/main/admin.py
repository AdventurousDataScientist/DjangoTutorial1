from django.contrib import admin
from .models import ToDoList
# need to get access to databases to see what is in them, avoid the .all and printing nonsense
admin.site.register(ToDoList) # see to do list database on admin site
# Register your models here.
