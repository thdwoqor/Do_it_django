from django.urls import path
from . import views
#python manage.py runserver
urlpatterns = [
    path('<int:pk>/',views.single_post_page),
    path('',views.index),
]