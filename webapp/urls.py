from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('proyectos', views.projects, name='projects'),
    path('planes', views.plans, name='plans'),
    path('sobre_mi', views.about, name='about'),
]