from django.shortcuts import render
from services.models import Service

def index(request):
  services = Service.objects.order_by('-date').filter(is_published=True)[:3]
  slides = Service.objects.order_by('-date').filter(is_slide=True)
  context = {
  'services': services,
  'slides': slides,
}
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def help(request):
  return render(request, 'help.html')