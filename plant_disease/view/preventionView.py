from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.Symptome import Symptome
from plant_disease.Model.prevention import prevention  # Ensure correct import path



# Liste des mesures préventives (Read - List)
class PreventionListView(ListView):
    model = prevention
    template_name = 'preventions/prevention_list.html'
    context_object_name = 'preventions'

# Détails d'une mesure préventive (Read - Detail)
class PreventionDetailView(DetailView):
    model = prevention
    template_name = 'preventions/prevention_detail.html'
    context_object_name = 'prevention'

# Créer une mesure préventive (Create)
class PreventionCreateView(CreateView):
    model = prevention
    fields = ['nom', 'description', 'symptômes_connexes']
    template_name = 'preventions/prevention_form.html'
    success_url = reverse_lazy('prevention-list')  # Adjust URL name as needed

# Mettre à jour une mesure préventive (Update)
class PreventionUpdateView(UpdateView):
    model = prevention
    fields = ['nom', 'description', 'symptômes_connexes']
    template_name = 'preventions/prevention_form.html'
    success_url = reverse_lazy('prevention-list')

# Supprimer une mesure préventive (Delete)
class PreventionDeleteView(DeleteView):
    model = prevention
    template_name = 'preventions/prevention_confirm_delete.html'
    success_url = reverse_lazy('prevention-list')