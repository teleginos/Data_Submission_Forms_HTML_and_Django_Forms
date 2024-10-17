from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def home_page(request):
    return render(request, "home_page.html")


def shop(request):
    return render(request, "shop.html")


def shopping_cart(request):
    return render(request, "shopping_cart.html")


def action_game(request):
    game_list = ["Red Dead Redemption II", "Elder Ring", "Black Myth: Wukong"]

    game_images = [
        "https://www.google.com/url?sa=i&url=http%3A%2F%2Ft3.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcTJGm-_E6Q1gD0HmglrtSEl1cWIyla1iCgHeRq9UPSwFnuvR_T3&psig=AOvVaw0eO-g3xTOf9Ds15DmcRhIz&ust=1729101702735000&source=images&cd=vfe&opi=89978449&ved=0CBMQjhxqFwoTCKD_8vf7kIkDFQAAAAAdAAAAABAE",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL9x_j3hcvdngtuJ2PGuRdT9zp7m7RH3iQgw&shttps://store.steampowered.com/app/1245620/ELDEN_RING/https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2FElden_Ring&psig=AOvVaw3sXAiDYwW8Wys_CHRoDXMm&ust=1729101828389000&source=images&cd=vfe&opi=89978449&ved=0CBMQjhxqFwoTCKCkgLX8kIkDFQAAAAAdAAAAABAE",
        "https://upload.wikimedia.org/wikipedia/ru/a/a6/Black_Myth_Wukong_cover_art.jpg",
    ]

    purchase_links = [
        "https://www.rockstargames.com/ru/reddeadredemption2",
        "https://en.bandainamcoent.eu/elden-ring/elden-ring",
        "https://www.heishenhua.com/",
    ]

    combined_data = zip(game_images, game_list, purchase_links)

    context = {
        "combined_data": combined_data,
    }

    return render(request, "game_action.html", context)


def adventure_game(request):
    game_list = ["Star Wars Jedi: Survivor", "Baldur's Gate 3", "Ведьмак 3: Дикая охота"]
    
    game_images = [
        "https://upload.wikimedia.org/wikipedia/ru/2/2e/Star_Wars_Jedi_-_Survivor.jpeg",
        "https://upload.wikimedia.org/wikipedia/ru/d/dc/Baldur%27s_Gate_III_Logo.png",
        "https://upload.wikimedia.org/wikipedia/ru/a/a2/The_Witcher_3-_Wild_Hunt_Cover.jpg"
    ]
    
    purchase_links = [
        "https://www.ea.com/ru-ru/games/starwars/jedi/jedi-survivor",
        "https://baldursgate3.game/",
        "https://www.thewitcher.com/us/ru/witcher3",
    ]
    
    combined_data = zip(game_images, game_list, purchase_links)

    context = {
        "combined_data": combined_data,
    }

    return render(request, "game_adventure.html", context)


def role_playing_game(request):
    game_list = ["Stardew Valley", "Dynasty Legends 2", "The Elder Scrolls V: Skyrim"]
    
    game_images = [
        "https://upload.wikimedia.org/wikipedia/en/f/fd/Logo_of_Stardew_Valley.png",
        "https://seagm-media.seagmcdn.com/game_480/3974.jpg?x-oss-process=image/resize,w_360",
        "https://images.ctfassets.net/rporu91m20dc/40dtTFlwPFBjdqdNgp1hLU/25a69c40fba0edf4008b7539373e5e14/Skyrim-AnnivEdition_Bnet_BoxArt_1200x1476-01.jpg",
    ]
    
    purchase_links = [
        "https://www.stardewvalley.net/",
        "https://dl2hmt.newtypegames.com/en/index.html",
        "https://elderscrolls.bethesda.net/en/skyrim10",
    ]
    
    combined_data = zip(game_images, game_list, purchase_links)

    context = {
        "combined_data": combined_data,
    }
    return render(request, "game_role_playing.html", context)
