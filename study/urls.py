from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('test/<int:id>/', views.study, name='study'),
    path('test/end', views.study1, name='study1'),
]