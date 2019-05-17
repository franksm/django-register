from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	return render(request,'test.html')
def a1link(request):
        return render(request,'a1.html')
# views.py
def showfood(request):
    food_list = Food.objects.all()
    context = {'food_list': food_list}
    return render(request, 'vendor/detail.html', context)
def singlefood(request, id):
    food_list = get_object_or_404(Food, id=id)
    context = {
        'food_list': food_list
    }
    return render(request, 'vendor/food_detail.html', context)
