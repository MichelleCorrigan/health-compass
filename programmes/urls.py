from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_programmes, name='programmes'),
    path('<int:programme_id>/', views.programme_detail, name='programme_detail'),
    path('add/', views.add_programme, name='add_programme'),
]
