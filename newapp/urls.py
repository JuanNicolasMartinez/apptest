from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('<int:id>/', views.get_task),
    path('create/', views.store_task),
    path('update/<int:id>/', views.update_task),
    path('delete/<int:id>/', views.delete_task)
]