from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('all/', views.GoodsList.as_view(), name='all'),
    path('item/<int:pk>/', views.GoodDetail.as_view(), name='detail'),
]