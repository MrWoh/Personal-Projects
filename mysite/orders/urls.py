from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('orders/', views.orders, name='orders'),
    path('calculations/', views.calculations, name='calculations'),
    path('supplier/', views.supplier, name='supplier'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('my_suppliers/', views.my_suppliers, name='my_suppliers'),
    path('contacts/', views.contacts, name='contacts'),
    path('new_items/', views.new_items, name='new_items'),
    path('invoices/', views.invoices, name='invoices'),

]
