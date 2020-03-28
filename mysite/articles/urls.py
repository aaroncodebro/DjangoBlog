from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.article_create, name="create"),
   path('<int:article_id>/', views.article_detail, name="detail"),
    path('edit/<int:article_id>/', views.article_edit, name="edit"),
    

]
