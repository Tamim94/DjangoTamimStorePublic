from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('blog/', views.post_list, name='post_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='store_logout'),

]
