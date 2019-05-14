"""web_empresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from core import views as core_views
from porta import views as porta_views
urlpatterns = [
	path('',core_views.home, name='home'),
	path('about',core_views.about, name='about'),
	path('blog',porta_views.porta, name='blog'),
	path('contact',core_views.contact, name='contact'),
	path('sample',core_views.sample, name='sample'),
	path('services',core_views.services, name='services'),
	path('store',core_views.store, name='store'),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)