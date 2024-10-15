"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task3.views import home_page, Shop, ShoppingCart, ActionGame, AdventureGame, RolePlayingGame

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('shop/', Shop.as_view()),
    path('shopping_cart/', ShoppingCart.as_view()),
    path('shop/game_action/', ActionGame.as_view()),
    path('shop/game_adventure/', AdventureGame.as_view()),
    path('shop/game_role_playing/', RolePlayingGame.as_view()),
]
