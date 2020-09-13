from django.shortcuts import render
from services.models import Service

def index(request):
  services = Service.objects.order_by('-date').filter(is_published=True)[:3]
  context = {
  'services': services,
}
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')