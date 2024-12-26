from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
 
urlpatterns = [
        path('', views.index, name ='index'),
        path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='user/password_reset.html',
            form_class=CustomPasswordResetForm
        ), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
         path('delete_account/', views.delete_account_request, name='delete_account'),
    path('verify_delete_account/', views.verify_delete_account, name='verify_delete_account'),
    path('account_deleted/', views.account_deleted, name='account_deleted'),
]
