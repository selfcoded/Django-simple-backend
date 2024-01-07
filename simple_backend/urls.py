from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('records/<int:num>/', views.custom, name='custom'),
    path('delete_item/<int:num>/', views.delete_item, name='delete_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:num>/', views.edit_item, name='edit_item'),
]