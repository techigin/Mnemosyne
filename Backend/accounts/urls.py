from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_user_view, name='login'),
    path('signup/', views.create_user_view, name='signup'),
    path('logout/', views.logout_user_view, name='logout'),
]
