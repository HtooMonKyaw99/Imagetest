from django.urls import path

from ocrapp import views
from ocrapp.views import home

urlpatterns = [
    path('',views.home, name='home'),
]
