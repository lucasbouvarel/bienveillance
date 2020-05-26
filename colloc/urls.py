from . import views
from django.conf.urls import url
from django.urls import include, path
urlpatterns = [
    path('vote', views.vote,name='vote'),
    path('connexion',views.connexion,name='connexion'),
    path('vote/<int:id>',views.voteid,name='voteid'),


]
