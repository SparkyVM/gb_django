"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import index, show_users, show_user_orders, last_days_orders, week_orders, month_orders, year_orders, add_item

urlpatterns = [
    path('', index, name='index'),
    path('users/', show_users, name='users'),
    path('users/<int:user_id>/', show_user_orders, name='user_orders'),
    path('orders/<int:days>/', last_days_orders, name='last_days_orders'),
    path('orders/week/', week_orders, name='week_orders'),
    path('orders/month/', month_orders, name='month_orders'),
    path('orders/year/', year_orders, name='year_orders'),
    path('item/', add_item, name='add_item')
]
