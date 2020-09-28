from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('all/', views.GoodsList.as_view(), name='all'),
    path('item/<int:pk>/', views.GoodDetail.as_view(), name='detail'),
    path('add/', views.CreateGood.as_view(), name='add'),
    path('update/<int:pk>/', views.GoodUpdate.as_view(), name='update'),
    path('remove/<int:pk>/', views.GoodDelete.as_view(), name='remove'),
]