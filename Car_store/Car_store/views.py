from django.shortcuts import render
from Car.models import Cars 
from brand_name.models import CarModel

def home(request, brand_slug=None):
    if brand_slug:
        carmodel = CarModel.objects.get(slug=brand_slug)
        data = Cars.objects.filter(brand_name=carmodel)
    else:
        data = Cars.objects.all()
    carmodels = CarModel.objects.all()
    return render(request, 'home.html', {'data': data, 'carmodel': carmodels})
