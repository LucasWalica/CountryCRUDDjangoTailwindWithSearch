from django.views.generic import View, DeleteView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Pais
from .forms import CountryCreateForm
from django.db.models import Q


class CountrySearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        countryList = Pais.objects.filter(
            Q(nombre__icontains = query) |
            Q(tipoDeGobierno__icontains= query) |
            Q(continente__icontains = query) |
            Q(moneda__icontains = query)
        )
        context = {
            'countryList':countryList
        }
        return render(request, 'busqueda_lista.html', context)


# Create your views here.
class CountryListView(View):
    def get(self, request, *args, **kwargs):
        countries = Pais.objects.all()
        context = {
            'countries':countries
        }
        return render(request, 'lista.html', context)
    
class CountryDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        country = get_object_or_404(Pais, pk=pk)
        context = {
            'country':country
        }
        return render(request, 'detalle.html', context)
    
class CountryCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CountryCreateForm()
        context = {
            'form':form
        }
        return render(request, 'crear_pais.html',context)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CountryCreateForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                fechaFundacion = form.cleaned_data.get('fechaFundacion')
                tipoGob = form.cleaned_data.get('tipoDeGobierno')
                poblacion = form.cleaned_data.get('poblacion')
                continente = form.cleaned_data.get('continente')
                PIB = form.cleaned_data.get('PIB')
                moneda = form.cleaned_data.get('moneda')
                p , data = Pais.objects.get_or_create(nombre = nombre, fechaFundacion = fechaFundacion, tipoDeGobierno = tipoGob, poblacion=poblacion, continente=continente, PIB=PIB, moneda=moneda)
                p.save()
                return redirect('paises')
        context = {}
        return render(request, 'crear_pais.html', context)
    
class CountryUpdateView(UpdateView):
    model = Pais
    fields = ['nombre', 'fechaFundacion', 'tipoDeGobierno', 'poblacion', 'continente', 'PIB', 'moneda']
    template_name = 'update_pais.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('detalle', kwargs={'pk':pk})       
    
    #does not work
class CountryDeleteView(DeleteView):
    model = Pais
    template_name = 'pais_delete.html'
    success_url = reverse_lazy('paises')
   
    