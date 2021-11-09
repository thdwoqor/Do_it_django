from django.urls import path
from . import views
#python manage.py runserver
urlpatterns = [
    path('about_me/',views.about_me),
    path('',views.landing),
]