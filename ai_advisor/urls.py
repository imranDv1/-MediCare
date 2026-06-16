from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_advisor, name='ai_advisor'),
    path('history/', views.consultation_history, name='consultation_history'),
    path('history/<int:pk>/', views.consultation_detail, name='consultation_detail'),
]
