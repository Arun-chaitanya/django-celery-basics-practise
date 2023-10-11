from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('result/<str:task_id>', views.check_result, name="check_result"),
]
