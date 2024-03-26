from django.urls import path 
from .views import CountryDetailView, CountryListView, CountryCreateView, CountryDeleteView, CountryUpdateView, CountrySearch

urlpatterns = [
    path('', CountryListView.as_view(), name='paises'),
    path('buscar/', CountrySearch.as_view(), name='paises_busqueda'),
    path('createPais/', CountryCreateView.as_view(), name='create'),
    path('<int:pk>/', CountryDetailView.as_view(), name='detalle'),
    path('<int:pk>/delete/', CountryDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', CountryUpdateView.as_view(), name='update')
    
]
