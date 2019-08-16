from django.shortcuts import render
from django.views.generic.edit import CreateView

from django.views import generic

from rest_framework import viewsets
from .serializers import CitySerializer


from .models import *
from django.db.models import Q


class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


def city_list(request):

    search_query_city = request.GET.get('search_city', '')
    search_query_street = request.GET.get('search_street', '')
    search_query_city = search_query_city.title()
    search_query_street = search_query_street.title()

    if search_query_city and search_query_street:
        length = Street.objects.filter(Q(name__icontains=search_query_street),
                                       Q(city__name__icontains=search_query_city))
        if length:
            return render(request, 'length.html', context={'length': length.values_list('length')})
        else:
            return render(request, 'exception.html')
    elif search_query_city:
        cities = City.objects.filter(Q(name__icontains=search_query_city)).values('name')
        streets = Street.objects.filter(city__name__in=cities)
        if streets:
            return render(request, 'street_list.html', context={'streets': streets.values_list('name')})
        else:
            return render(request, 'exception.html')
    elif search_query_street:
        street = Street.objects.filter(Q(name__icontains=search_query_street)).values('name')
        cities = City.objects.filter(street__name__icontains=street)
        if cities:
            return render(request, 'city_list.html', context={'cities': cities})
        else:
            return render(request, 'exception.html')
    else:
        return render(request, 'base.html')


class CityDetailView(generic.DetailView):
    model = City
    template_name = 'city_detail.html'
    context_object_name = 'city'


class StreetDetailView(generic.DetailView):
    model = Street
    template_name = 'street_detail.html'
    context_object_name = 'street'


class CityCreate(CreateView):
    model = City
    template_name = 'city_create.html'
    fields = '__all__'


class StreetCreate(CreateView):
    model = Street
    template_name = 'street_create.html'
    fields = '__all__'


