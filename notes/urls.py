"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from notes import views,api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notes', api_views.NotesViewSet)


urlpatterns = [    
    
   path('', views.NotesList.as_view(),name="notes.list"),
   path('api/', include(router.urls)),   
   path('<int:pk>', views.NotesDetail.as_view(), name="notes.detail"),
   path('<int:pk>/edit/', views.NotesUpdate.as_view(), name="notes.update"),
   path('<int:pk>/delete/', views.NotesDelete.as_view(), name="notes.delete"),
   path('new/', views.NotesCreate.as_view(), name="notes.new")
   
]
