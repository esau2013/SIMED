from django.urls import path
from agiosaude.accounts import views as acc_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_view.LogoutView.as_view(next_page='core:home'), name='logout'),
]