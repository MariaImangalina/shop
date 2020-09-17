from django.urls import path
from . import views

app_name='orders'

urlpatterns = [
    path('summary/', views.OrderSummary.as_view(), name='summary'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('plus_qty/<int:pk>', views.plus_qty, name='plus_qty'),
    path('minus_qty/<int:pk>', views.minus_qty, name='minus_qty'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
]