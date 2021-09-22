from django.contrib import admin
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home,name='home'),
    path('orders/',views.orders,name='orders'),
    path('products/',views.products,name='products'),
    path('customer/<pk>',views.customer,name='customer'),

    path('register/',views.register_page,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('user/',views.userpage,name='user-home'),

    path('password_reset', auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),

    path('password_reset_sent', auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),

    path('password/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),

    path('password_reser_done', auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete')
]