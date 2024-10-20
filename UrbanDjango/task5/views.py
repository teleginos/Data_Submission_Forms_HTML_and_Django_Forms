from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

users_dict = {}

class User():
    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age

def sign_up_by_html(request):
    info = {'err': []}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users_dict:
            info['err'].append('Пользователь с таким именем уже существует')
        
        if password != repeat_password:
            info['err'].append('Пароли не совпадают')
        
        if int(age) < 18:
            info['err'].append('Вы не достигли 18 лет')
        
        if not info['err']:
            users_dict[username] = User(username, password, int(age))
            info['success_message'] = f'Приветствуем, {username}'
    

    context = {
        'info': info
    }
    
    return render(request, 'registration_page.html', context)

def sign_up_by_django(request):
    info = {'err': []}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users_dict:
                info['err'].append('Пользователь с таким именем уже существует')
            
            if password != repeat_password:
                info['err'].append('Пароли не совпадают')
            
            if int(age) < 18:
                info['err'].append('Вы не достигли 18 лет')
            
            if not info['err']:
                users_dict[username] = User(username, password, int(age))
                info['success_message'] = f'Приветствуем, {username}'
    
    else:
        form = UserRegister()


    context = {
        'info': info,
        'form': form,
    }
    return render(request, 'registration_page.html', context)