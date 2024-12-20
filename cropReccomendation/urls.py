from django.urls import path
from . import views


urlpatterns = [
    path('', views.predictCrop, name="predictCrop"),
]
