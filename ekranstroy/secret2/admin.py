from django.contrib import admin

from .models import *

# class LineInline(admin.TabularInline):
#     model = Line
#     extra = 1  # Количество пустых форм для добавления новых книг

@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'description', 'slug']
    # inlines = [LineInline]

@admin.register(Purchased)
class PurchasedAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'title', 'amount', 'unit', 'price', 'total_price', 'estimate']
    list_filter = ['estimate']
    ordering = ['id']

@admin.register(Completed)
class CompletedAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'title', 'amount', 'unit', 'price', 'total_price', 'estimate']
    list_filter = ['estimate']
    ordering = ['id']

@admin.register(Paid)
class PaidAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'title', 'amount', 'unit', 'price', 'total_price', 'estimate']
    list_filter = ['estimate']
    ordering = ['id']

    # def total_price2(self, obj):
    #     return round(float(obj.total_price), 3)
    # total_price2.short_description = 'Total Price2'
