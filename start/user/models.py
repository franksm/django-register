#coding:utf-8

from django.db import models
from django.contrib import admin

# Create your models here.
class Doctor(models.Model):

	name = models.CharField(max_length = 20) # 名稱
	address = models.CharField(max_length = 100) # 地址

	def __str__(self):
		return self.name

	class Meta:  
		permissions = (('can_view','Can view doctor'), 
                       ('can_add','Can add doctor'),
					   ('can_see','Can see doctor'),
                       ('can_edit','Can edit doctor'),
                       ('can_delete','Can delete doctor'))


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Doctor._meta.fields]


