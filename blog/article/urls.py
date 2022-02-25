from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('a_index/', views.a_index, name='a_index'),
    path('a_detail/<int:id>/', views.a_detail, name='a_detail'),
    path('a_create/', views.a_create, name='a_create'),
    path('a_delete/<int:id>/', views.a_delete, name='a_delete'),
    path('a_modify/<int:id>/', views.a_modify, name="a_modify"),
]