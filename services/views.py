from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Service

def index(request):
  services = Service.objects.all().order_by('-date')
  paginator = Paginator(services, 6)
  page = request.GET.get('page')
  paged_services = paginator.get_page(page)
  context = {
    'services': paged_services
  }
  return render(request, 'services.html', context)

def service(request, service_id):
  service = get_object_or_404(Service, pk=service_id)
  context = {
    'service': service
  }
  return render(request, 'service.html', context)