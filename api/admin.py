from django.contrib import admin
from api.models import User, Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(User)
