#coding:utf-8

from django.db import models
from django.contrib import admin

# Create your models here.
class Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址
	
	def __str__(self):
		return self.vendor_name
class Food(models.Model):
	food_name = models.CharField(max_length = 30) # 食物名稱
	price_name = models.DecimalField(max_digits = 3, decimal_places=0) # 食物價錢
	food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的 
	
	def __str__(self):
		return self.food_name

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Food._meta.fields]
	# 過濾 price_name
	list_filter = ('price_name',)
	fields = ['price_name'] # 顯示欄位
	search_fields = ('food_name','price_name')
	ordering = ('price_name',) # 價格 由小到大 排序
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Vendor._meta.fields]

from django.db import models

class Person(models.Model):
 schoolClass = models.CharField(max_length=20) # 班級
 className = models.CharField(max_length=20) # 班級名稱
 schoolClassChinese = models.CharField(max_length=20) # 班級名稱1
 seatNumber = models.CharField(max_length=20) # 座號
 studentID = models.CharField(max_length=20) # 學號
 name = models.CharField(max_length=30) # 姓名
 identityCard = models.CharField(max_length=30) # 身分證
 sex = models.CharField(max_length=2)  # 性別
 birth_date = models.CharField(max_length=20) # 出生日期
