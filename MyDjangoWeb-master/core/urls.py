"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from .views import hi, r, tag_test

from practice1 import views


urlpatterns = [
    path('hi/<int:n1>/<int:n2>/', hi),
    path('r/<int:start>/<int:stop>/', r),
    path('tag_test/', tag_test),
    path('admin/', admin.site.urls),

    path('posts/', views.index, name='posts_index'),
    path('posts/new/', views.new, name='posts_new'),
    path('posts/<int:pk>/', views.show, name='posts_show'),
    path('posts/<int:pk>/edit/', views.edit, name='posts_edit'),
    path('posts/<int:pk>/delete/', views.delete, name='posts_delete'),
]
