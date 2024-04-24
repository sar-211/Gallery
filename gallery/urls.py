from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('edit_field/<int:pk>/', views.edit, name='edit'),
    path('delete_image/<int:pk>', views.delete, name = 'delete')
    
]