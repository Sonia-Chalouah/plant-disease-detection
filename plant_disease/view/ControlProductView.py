from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.ControlProduct import ControlProduct

# Liste des produits de contrôle (Read - List)
class ControlProductListView(ListView):
    model = ControlProduct
    template_name = 'control_products/controlproduct_list.html'
    context_object_name = 'control_products'

# Détails d'un produit de contrôle (Read - Detail)
class ControlProductDetailView(DetailView):
    model = ControlProduct
    template_name = 'control_products/controlproduct_detail.html'
    context_object_name = 'control_product'

# Créer un produit de contrôle (Create)
class ControlProductCreateView(CreateView):
    model = ControlProduct
    fields = ['nom', 'type', 'description', 'méthode_application', 'efficacité', 'pests']
    template_name = 'control_products/controlproduct_form.html'
    success_url = reverse_lazy('controlproduct-list')

# Mettre à jour un produit de contrôle (Update)
class ControlProductUpdateView(UpdateView):
    model = ControlProduct
    fields = ['nom', 'type', 'description', 'méthode_application', 'efficacité', 'pests']
    template_name = 'control_products/controlproduct_form.html'
    success_url = reverse_lazy('controlproduct-list')

# Supprimer un produit de contrôle (Delete)
class ControlProductDeleteView(DeleteView):
    model = ControlProduct
    template_name = 'control_products/controlproduct_confirm_delete.html'
    success_url = reverse_lazy('controlproduct-list')
