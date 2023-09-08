from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.record, name='record'),
    path('delete/<int:pk>/', views.delete_user, name='delete'),
    path('add_record/', views.add_record, name='add_record'),
    path('update/<int:pk>/', views.update, name='update'),
]
