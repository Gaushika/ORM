from django.db import models
from django.contrib import admin
class car(models.Model):
    mod_num=models.IntegerField(primary_key=True)
    car_name=models.CharField(max_length=20)
    car_color=models.CharField(max_length=20)
    car_num=models.IntegerField()
    price=models.IntegerField()
class carAdmin(admin.ModelAdmin):
    list_display=["mod_num","car_name","car_color","car_num","price"]
    

