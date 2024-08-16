from django.contrib import messages  
from django.shortcuts import redirect, render
from .models import Pet,logincredentials 
from django.http import HttpResponse,JsonResponse

def home(request):
    category = request.GET.get('category', None)
    query = request.GET.get('search', None)
    pets = Pet.objects.all()
    if category:
        pets = pets.filter(Category=category)
    if query:
        pets = pets.filter(name__icontains=query)
    context = {'pets': pets,'selected_category': category,'query': query,}
    return render(request, "myapp/home.html", context)

def store_id(request):
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        print("ID:", pet_id)
        response = redirect('store_id_page')
        response.set_cookie('pet_id', pet_id)
        return response
    else:
        return HttpResponse("Method not allowed.")

def store_id_page(request):
    pet_id = request.COOKIES.get('pet_id')
    required_pet = Pet.objects.get(id=pet_id)
    context = {'required_pet': required_pet}
    return render(request, "myapp/store_id.html",context) 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = logincredentials.objects.get(username=username, password=password)
            response = redirect('home')
            response.set_cookie('username', username)
            return response
        except logincredentials.DoesNotExist:
            return render(request, 'myapp/login.html', {'invalid_credentials': True})
    return render(request, 'myapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        if logincredentials.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
        if logincredentials.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('register')
        new_user = logincredentials(username=username, password=password, email=email)
        new_user.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')
    return render(request, 'myapp/register.html')
    
def logout_view(request):
    response = redirect('/login')
    response.delete_cookie('username') 
    response.set_cookie('pet_id')
    return response

def update_like_dislike(request):
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        action = request.POST.get('action')
        pet = Pet.objects.get(id=pet_id)
        if action == 'like':
            pet.like += 1
        elif action == 'dislike':
            pet.dislike += 1
        pet.save()
        return JsonResponse({'success': True, 'like': pet.like, 'dislike': pet.dislike})
    return JsonResponse({'success': False})


def add_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        breed = request.POST.get('breed')
        url = request.POST.get('url')
        weight = request.POST.get('weight')
        category = request.POST.get('category')

        new_pet = Pet(name=name,age=age,breed=breed,url=url,weight=weight,Category=category)
        new_pet.save()
        messages.success(request, 'Pet added successfully.')
        return redirect('home')
    return render(request, 'myapp/addpet.html')

def remove_pet(request):
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        try:
            pet = Pet.objects.get(id=pet_id)
            pet.delete()
            messages.success(request, 'Pet removed successfully.')
        except Pet.DoesNotExist:
            messages.error(request, 'Pet not found.')
        return redirect('home')
    else:
        return HttpResponse("Method not allowed.")