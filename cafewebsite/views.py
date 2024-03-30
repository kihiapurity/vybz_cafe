# VybzCafeProject\cafewebsite\views.py

from rest_framework import generics
from .models import Menu, Update, HomePageSettings
from .serializers import MenuSerializer, UpdateSerializer, HomePageSettingsSerializer
from django.shortcuts import render, get_object_or_404
from .models import HomePageSettings
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from django.http import JsonResponse
from django.views.generic import DetailView



class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


def home_settings(request):
    home_settings = HomePageSettings.objects.first()
    return render(request, 'home_settings.html', {'home_settings': home_settings})


class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UpdateListCreate(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

def menu_details(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    data = {
        'name': menu_item.name,
        'description': menu_item.description,
        'ingredients': menu_item.ingredients,
        'price': menu_item.price,
    }
    return JsonResponse(data)

def home(request):
    menus = Menu.objects.all().prefetch_related('images')
    updates = Update.objects.all()
    home_settings = HomePageSettings.objects.first()
    return render(request, 'home.html', {'menus': menus, 'updates': updates, 'home_settings': home_settings})


class MenuDetailsView(DetailView):
    model = Menu
    template_name = 'menu_details.html'  # You can create this template if needed

    def render_to_response(self, context, **response_kwargs):
        # Customize the JSON response based on the menu item details
        menu_item = context['object']
        data = {
            'name': menu_item.name,
            'description': menu_item.description,
            'ingredients': menu_item.ingredients,
            'price': menu_item.price,
            # Add more fields as needed
        }
        return JsonResponse(data)
    

def about_us(request):
    home_settings = HomePageSettings.objects.first()
    return render(request, 'about_us.html', {'home_settings': home_settings})

def footer(request):
    # Add your code for rendering the footer view here
    return render(request, 'footer.html')
