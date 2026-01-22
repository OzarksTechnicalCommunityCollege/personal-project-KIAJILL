from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
path('', views.horse_list, name='horse_list'),
path('<int:id>/', views.horse_detail, name='horse_detail'),
]

