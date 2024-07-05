from django.contrib import admin
from .models import Item, User, Order
from random import choice

@admin.action(description="Изменить город")
def set_city(modeladmin, request, queryset):
    queryset.update(adr = "Москва")

@admin.action(description="Обнулить количество")
def set_zero(modeladmin, request, queryset):
    queryset.update(count = 0)

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','date_add']
    ordering = ['name']
    list_filter = ['date_add']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    actions = [set_city]

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    ordering = ['-price']
    list_filter = ['date_add']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по названию'
    actions = [set_zero]
    readonly_fields = ['date_add']
    fieldsets = [
        (
            'Инфо о товаре',
            {
                'classes': ['wide'],
                'fields': ['name', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            },
        ),
        (
            'Прочее',
            {   
                'classes': ['collapse'],
                'fields': ['date_add', 'img'],
            }
        ), ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'item_id', 'price','date_add']
    ordering = ['user_id', 'item_id']
    list_filter = ['date_add']
    
# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)