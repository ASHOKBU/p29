from django.urls import path
app_name="myapp"
from myapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
