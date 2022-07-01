from django.contrib import admin
from .models import Supplier, Order, Categories
from django.db.models import Count


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'unit', 'order_code', 'note')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'email', 'phone')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("category", "order_count")

    def order_count(self, obj):
        return obj._order_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _order_count=Count("order", distinct=True),)
        return queryset


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Categories, CategoriesAdmin)
