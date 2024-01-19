from django.shortcuts import render

def main(request):
	context = {}
	return render(request, 'store/main.html', context)

def mens(request):
	context = {}
	return render(request, 'store/mens.html', context)

def home(request):
	context = {}
	return render(request, 'store/home.html', context)

def Contact(request):
	context = {}
	return render(request, 'store/Contact.html', context)

