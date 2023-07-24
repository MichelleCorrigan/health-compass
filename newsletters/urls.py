from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletters, name='newsletters'),
    path('sign_up/', views.newsletter_signup, name='newsletter_signup'),
    path('unsubscribe/', views.newsletter_unsubscribe,
         name='newsletter_unsubscribe'),
]
