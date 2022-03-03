from django.urls import path
from . import views


urlpatterns = [
    path('', views.Liste_of_pv),
    path('tache/', views.Liste_of_taches),
    path('membres/', views.Liste_of_membres),

    #INSERTING
    path('addpv/', views.addPV),
    path('addmembre/', views.addMembre),
    path('addtache/', views.addTache),

]
