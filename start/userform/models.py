from django.db import models
from django.contrib import admin

# Create your models here.

class UserProfile(models.Model):

	name = models.CharField(max_length = 20) # 名稱
	address = models.CharField(max_length = 100) # 地址

	def __str__(self):
		return self.name

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = [field.name for field in UserProfile._meta.fields]

