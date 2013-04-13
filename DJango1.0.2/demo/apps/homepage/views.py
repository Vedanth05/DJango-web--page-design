#from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('homepage/index.html')

def about(request):
	return render_to_response('homepage/about.html')


def books(request):
	return render_to_response('homepage/books.html')

def projects(request):
	return render_to_response('homepage/projects.html')

def contact(request):
	return render_to_response('homepage/contact.html')

