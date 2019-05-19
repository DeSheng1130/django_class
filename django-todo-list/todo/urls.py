from django.urls import path

from . import views as v


app_name = 'todo'
urlpatterns = [
    path('', v.index, name='index'),
    path('new/', v.new, name='new'),
    path('<int:pk>/', v.show, name='show'),
    path('<int:pk>/edit/', v.edit, name='edit'),
    path('<int:pk>/delete/', v.delete, name='delete'),
]