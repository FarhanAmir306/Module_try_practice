from django.urls import path
from .import views
app_name='author'
urlpatterns = [
    path('register/',views.add_register,name='register'),
    # path('login/',views.user_login,name='login'),
    path('login/',views.MyLoginView.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('update/profile/',views.update_profile,name='update_profile'),
    path('logout/',views.User_logout,name='logout'),
    path('changepass/',views.change_password,name='changepass'),

]
