from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  plant_disease.Model.typePlant import TypePlante

# Liste des types de plantes (Read - List)
class TypePlanteListView(ListView):
    model = TypePlante
    template_name = 'type_plante/typeplante_list.html'
    context_object_name = 'plantes'

# Détails d'un type de plante (Read - Detail)
class TypePlanteDetailView(DetailView):
    model = TypePlante
    template_name = 'type_plante/typeplante_detail.html'
    context_object_name = 'plante'

# Créer un type de plante (Create)
class TypePlanteCreateView(CreateView):
    model = TypePlante
    fields = ['nom', 'description', 'image']
    template_name = 'type_plante/typeplante_form.html'
    success_url = reverse_lazy('typePlantes-list')

# Mettre à jour un type de plante (Update)
class TypePlanteUpdateView(UpdateView):
    model = TypePlante
    fields = ['nom', 'description', 'image']
    template_name = 'type_plante/typeplante_form.html'
    success_url = reverse_lazy('typePlantes-list')

# Supprimer un type de plante (Delete)
class TypePlanteDeleteView(DeleteView):
    model = TypePlante
    template_name = 'type_plante/typeplante_confirm_delete.html'
    success_url = reverse_lazy('typePlantes-list')
