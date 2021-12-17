"""parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from space_app.views import index, reserving, editing, logout, approving,\
    ReservationsListView, ReservationsCreateView, ReservationsDeleteView, ReservationsUpdateView,\
    SpacesCreateView, SpacesListView, SpacesDeleteView, SpacesUpdateView


urlpatterns = [
    path('', index, name='index'),
    path('reserving/', reserving, name='reserving'),
    path('editing/', editing, name='editing'),
    path('admin/', admin.site.urls),
    path('logout/', logout, name='logout'),
    path('approving/<str:space_name>/<str:reservation_time>', approving, name='approving'),

    path('reservations-read/', ReservationsListView.as_view(), name='reservations-read'),
    path('reservations-create/', ReservationsCreateView.as_view(), name='reservations-create'),
    path('reservations-update/<int:pk>/', ReservationsUpdateView.as_view(), name='reservations-update'),
    path('reservations-remove/<int:pk>/', ReservationsDeleteView.as_view(), name='reservations-remove'),

    path('spaces-read/', SpacesListView.as_view(), name='spaces-read'),
    path('spaces-create/', SpacesCreateView.as_view(), name='spaces-create'),
    path('spaces-update/<int:pk>/', SpacesUpdateView.as_view(), name='spaces-update'),
    path('spaces-remove/<int:pk>/', SpacesDeleteView.as_view(), name='spaces-remove'),
]
