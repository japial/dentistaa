from django.contrib import admin

from doctors.models import TreatmentCategory, Treatment, Doctor, Chamber


@admin.register(Doctor)
class DentistAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(TreatmentCategory)
class TreatmentCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ['name', 'category']
    list_filter = ['category']


@admin.register(Chamber)
class ChamberAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ['name']





