from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),




    path('machine/add',views.MachineCreate.as_view(),name='add-machine'),

     
    path('machine/<int:pk>/edit/',views.MachineUpdate.as_view(),name='edit-machine'),


    path('machine/<int:pk>/delete/',views.MachineDelete.as_view(),name='delete-machine'),
    

]