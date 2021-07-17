from django.urls import path, re_path
from register import views
urlpatterns = [
    path('', views.index, name='home'),
    path('singup', views.Register_user, name='singup'),
    path('singin', views.login_user, name='singin'),
    path('registration/success', views.success_message, name='success_message'),
    path('registration/failed', views.failed_message, name='failed_message'),
    path('profile/<slug:user_slug>', views.user_detail, name='profile'),
]
