"""medibot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from mainapp import views as mainapp_views
from adminapp import views as adminapp_views
from userapp import views as userapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # main
    path('', mainapp_views.index, name='index'),
    path('about', mainapp_views.about, name='about'),
    path('doctor', mainapp_views.doctor, name='doctor'),
    path('services', mainapp_views.services, name='services'),
    path('contact', mainapp_views.contact, name='contact'),
     
    # user
    path('user-login',userapp_views.user_login,name='user_login'),
    path('user-registration', userapp_views.user_registration, name='user_registration'),
    path('user-logout', userapp_views.user_logout, name='user_logout'),
    path('user-dashboard', userapp_views.user_dashboard, name='user_dashboard'),
    path('user-feedback', userapp_views.user_feedback, name='user_feedback'),
    path('user-medibot', userapp_views.user_medibot, name='user_medibot'),
    path('user-myprofile', userapp_views.user_myprofile, name='user_myprofile'),
    path('viewed', userapp_views.viewed, name='viewed'),
    
    #admin
    path('admin-login', adminapp_views.admin_login, name='admin_login'),
    path('admin-logout', adminapp_views.admin_logout, name='admin_logout'),
    path('admin-all-user', adminapp_views.admin_all_user, name='admin_all_user'),
    path('admin-dashboard', adminapp_views.admin_dashboard, name='admin_dashboard'),
    # path('admin-disease-report', adminapp_views.admin_disease_report, name='admin_disease_report'),
    # path('admin-feedback-analysis', adminapp_views.admin_feedback_analysis, name='admin_feedback_analysis'),
    path('admin-interaction', adminapp_views.admin_interaction, name='admin_interaction'),
    path('admin-pending-user', adminapp_views.admin_pending_user, name='admin_pending_user'),
    path('admin-sentiment-analysis', adminapp_views.admin_sentiment_analysis, name='admin_sentiment_analysis'),
    path('admin-user-feedback', adminapp_views.admin_user_feedback, name='admin_user_feedback'),
    path('update/<int:id>/', adminapp_views.update, name='update'),
    path('reject/<int:id>/', adminapp_views.reject, name='reject'),
    path('search', adminapp_views.search, name='search'),
    path('searcha', adminapp_views.searcha, name='searcha'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

