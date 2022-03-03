from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.HomePage, name='homepage'),
    path('creation/',views.CreationPage, name='creation'),
    path('listepv/',views.ListePV, name='listepv'),
    path('pv/<str:pk>/',views.PVpage, name='pvpage'),


    #inserting
    path('addpv/', views.addPV, name='addpv'),
    path('addtache/', views.addtache, name='addtache'),
    path('addmembre/', views.addmembre, name='addmembre'),

    #deleting
    path('deletetache/<str:pk>/', views.deletetache, name='deletetache'),

]
