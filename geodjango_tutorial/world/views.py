from django.shortcuts import render, redirect
from .models import WorldBorder, Profile as user
from .models import CountryInfo

# authentication
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

from django.contrib.gis.geos.point import Point
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def country_info(request):
    user_profile = user.objects.get(user=request.user)
    location = user_profile.location
    country = WorldBorder.objects.get(mpoly__contains=user_profile.location)
    country_name = country.name
    print(country_name)
    country_info = CountryInfo.objects.get(country=country_name)
    context = {
                    'country': country_info.country,
                    'region': country_info.region,
                    'popDensity': country_info.population,
                    'area': country_info.area,
                    'gdp': country_info.gdp,
                    'birthrate': country_info.birthrate,
                    'deathrate': country_info.deathrate,
                    'infantMort': country_info.infantMort,
                    'literacy': country_info.literacy,
                    'phones': country_info.phones,
                    'arable': country_info.arable,
                    'crops': country_info.crops,
                    'other': country_info.other,
                    'climate': country_info.climate,
                    'agriculture': country_info.agriculture,
                    'industry': country_info.industry,
                    'service': country_info.service,
                }
    return render(request, 'country_info.html', context)
# Create your views here.
def index_view(request):
    return render(request, 'base.html')
# View that reads the locations from world borders and passes on to maps
def map_view(request):
    # expand the code by setting the authentication here
    if request.user.is_authenticated:
        user_profile = user.objects.get(user=request.user)
        location = user_profile.location
        try:
            country = WorldBorder.objects.get(mpoly__contains=user_profile.location)
            country_name = country.name
        except WorldBorder.DoesNotExist:
            country_name = "Unknown Location"
        return render(request, 'map.html', {'user': request.user, 'location': location, 'country_name' : country_name})
    else:
        return render(request, 'login.html')
    

#login & logout views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('world:index')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

#Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def update_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        user = request.profile
        user.location = Point(float(longitude), float(latitude))
        user.save()
        try:
            country = WorldBorder.objects.get(mpoly__contains=user_profile.location)
            country_name = country.name
        except WorldBorder.DoesNotExist:
            country_name = "Unknown Location"
        return JsonResponse({'success': True, 'country': country_name})
    return JsonResponse({'success': False})

