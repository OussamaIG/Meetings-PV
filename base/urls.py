from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.HomePage, name='homepage'),
    path('listepv/',views.ListePV, name='listepv'),
    path('pv/<str:pk>/',views.PVpage, name='pvpage'),


    #inserting
    path('addpv/', views.addPV, name='addpv'),
    path('addtache/', views.addtache, name='addtache'),
    path('addmembre/', views.addmembre, name='addmembre'),

    #deleting
    path('deletepv/<str:pk>/', views.deletepv, name='deletepv'),
    path('deletetache/<str:pk>/', views.deletetache, name='deletetache'),
    path('deletemember/<str:pk>/', views.deletemember, name='deletemember'),

    #editing
    path('addmembertopv/<str:pk>/', views.addmembertopv, name='addmembertopv'),
    path('addtachetopv/<str:pk>/', views.addtachetopv, name='addtachetopv'),

]
