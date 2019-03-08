from django.shortcuts import render
from .models import *
# Create your views here.
def index(request) :

	cats=Cat.objects.all()
	
	for cat in cats :
		print(cat.image)

	context = {'cats_key' : cats}

	return render(request, './index.html', context)


def test(request) :

	return render(request, './test.html')