from django.urls import path
from . import views


urlpatterns = [
    path('', views.predictFertilizer, name="predictCrop"),
]
