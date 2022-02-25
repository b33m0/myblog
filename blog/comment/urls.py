from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('c_create/<int:article_id>/', views.c_create, name='c_create'),
    path('c_delete/<int:a_id>/<int:c_id>/', views.c_delete, name='c_delete'),

]