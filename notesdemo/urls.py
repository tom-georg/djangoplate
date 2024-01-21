

"""
URL configuration for djangoplate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from notesdemo.views import index, NoteCreateView, NoteListView, NoteDetailView, NoteUpdateView

app_name = "notesdemo"

urlpatterns = [
    path('index/', index.as_view(), name='index'),
    path('notes/create/', NoteCreateView.as_view(), name='create'),
    path('notes/', NoteListView.as_view(), name='list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='update'),

]
