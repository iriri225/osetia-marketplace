from django.shortcuts import render
from shops.models import Shop

def index(request):
    shops = Shop.objects.all()
    return render(request, 'index.html', {'shops': shops})