from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_task, name= 'show'),
    path('add/', views.add_task, name= 'add'),
    path('delete/<int:id>', views.delete_task, name= 'delete'),
    path('delete_complete/<int:id>', views.delete_complete_task, name= 'delete_complete'),
    path('edit/<int:id>', views.edit_task, name= 'edit'),
    path('all_complete/', views.all_complete_task, name= 'all_complete'),
    
    path('complete/<int:id>', views.complete_task, name= 'complete'),
]
