from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def home_page(request):
    return render(request, "home_page.html")


class Shop(TemplateView):
    template_name = "shop.html"


class ShoppingCart(TemplateView):
    template_name = "shopping_cart.html"


class ActionGame(TemplateView):
    template_name = "game_action.html"


class AdventureGame(TemplateView):
    template_name = "game_adventure.html"


class RolePlayingGame(TemplateView):
    template_name = "game_role_playing.html"
