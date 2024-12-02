from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]
#path('admin/', admin.site.urls),
#    path('', include('website.urls')),