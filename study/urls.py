from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('study/<int:id>/', views.study, name='study'),
    #path('2', views.study1, name='study1'),
]