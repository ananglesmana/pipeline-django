from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def index (request):
	
	context = {
	'nama' : 'Anang Lesmana',
	'age'  : '23'
	}
	return render (request, 'index.html' ,context)

def profil(request):
	return render (request, 'profil.html')

def data(request):
	post = Post.objects.all()
	
	context = {
	'Post':post,
	}
	
	return	render (request, 'data.html', context)
