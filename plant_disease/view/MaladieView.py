from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.maladie import Maladie

# Liste des maladies FrontOffice(Read - List)
class MaladieListFrontView(ListView):
    model = Maladie
    template_name = 'maladies/Maladies.html'
    context_object_name = 'maladies'
# Liste des maladies (Read - List)
class MaladieListView(ListView):
    model = Maladie
    template_name = 'maladies/maladie_list.html'
    context_object_name = 'maladies'
class MaladieDetailfrontView(DetailView):
    model = Maladie
    template_name = 'maladies/maladie_detailfront.html'  # This is the template we created
    context_object_name = 'maladie'        # The object name to use in the template

# Détails d'une maladie (Read - Detail)
class MaladieDetailView(DetailView):
    model = Maladie
    template_name = 'maladies/maladie_detail.html'
    context_object_name = 'maladie'

# Créer une maladie (Create)
class MaladieCreateView(CreateView):
    model = Maladie
    fields = ['nom', 'description', 'type', 'plantes']  # Include the M2M relation with Plante
    template_name = 'maladies/maladie_form.html'
    success_url = reverse_lazy('maladie-list')

# Mettre à jour une maladie (Update)
class MaladieUpdateView(UpdateView):
    model = Maladie
    fields = ['nom', 'description', 'type', 'plantes']  # Include the M2M relation with Plante
    template_name = 'maladies/maladie_form.html'
    success_url = reverse_lazy('maladie-list')

# Supprimer une maladie (Delete)
class MaladieDeleteView(DeleteView):
    model = Maladie
    template_name = 'maladies/maladie_confirm_delete.html'
    success_url = reverse_lazy('maladie-list')
