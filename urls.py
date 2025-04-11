"""
URL configuration for table_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from table_management.views import table_list, reservation_list, reservation_create, reservation_detail, \
    reservation_edit, reservation_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tables/', table_list, name='table_list'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/create/', reservation_create, name='reservation_create'),
    path('reservations/<int:reservation_id>/', reservation_detail, name='reservation_detail'),
    path('reservations/edit/<int:reservation_id>/', reservation_edit, name='reservation_edit'),
    path('reservations/delete/<int:reservation_id>/', reservation_delete, name='reservation_delete'),
]