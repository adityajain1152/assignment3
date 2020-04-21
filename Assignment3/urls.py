from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
path('admin/', admin.site.urls),

path('home/', include('inventory.urls')),

path('', views.loginPage, name='login'),

path('register/', views.registerPage, name='register'),

path('logout/', views.logoutUser, name="logout"),

]
