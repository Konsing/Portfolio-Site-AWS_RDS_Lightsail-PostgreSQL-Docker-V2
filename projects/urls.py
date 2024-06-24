from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('contact/', views.contact_view, name='contact'),
]
