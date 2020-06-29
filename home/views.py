from django.shortcuts import render
import os

def index(request):
  context = {
    't': os.environ.get('TEST', 'default')
  }
  return render(request, 'home/index.html', context)
