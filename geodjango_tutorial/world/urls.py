from django.urls import path
from . import views

app_name = 'world'
urlpatterns = [
    path('index', views.index_view, name='index'),
    path('map/', views.map_view, name='map'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('update_location/', views.update_location, name='update_location'),
    path('country_info/', views.country_info, name='country_info'),
]
