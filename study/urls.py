from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('test/<int:id>/<int:idU>', views.study, name='study'),
    path('test/end/<int:idU>', views.study1, name='study1'),
]