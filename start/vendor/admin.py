from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Vendor,Food,Person

# Register your models here.
#admin.site.register(Vendor)
#admin.site.register(Food)
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
 list_display = ('id' or 'ID', 'schoolClass', 'className', 'schoolClassChinese', 'seatNumber', 'studentID', 'name', 'identityCard', 'sex', 'birth_date')
