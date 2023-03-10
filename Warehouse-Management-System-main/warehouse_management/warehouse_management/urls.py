"""warehouse_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app_views.home,name='home'),
    path('login/',app_views.login,name='login'),
    path('map/',app_views.stock_chart_view,name='map'),
    path('db/',app_views.dbtest,name='db'),
    path('createuser/',app_views.createuser,name='createuser'),
    path('admins/',app_views.admin,name='admindb'),
    path('entry/',app_views.entry,name='entry'),
    path('report/',app_views.report,name='report'),
    path('prophet/',app_views.prophet,name='prophet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
