from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('delete/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]
