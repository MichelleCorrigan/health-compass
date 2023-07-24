from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.newsletter_signup, name='newsletter_signup'),
    path('unsubscribe/', views.newsletter_unsubscribe,
         name='newsletter_unsubscribe'),
]
