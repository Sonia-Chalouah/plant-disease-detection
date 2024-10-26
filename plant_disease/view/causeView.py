# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.cause import CauseMaladie


# List view for Cause Maladie
class CauseMaladieListView(ListView):
    model = CauseMaladie
    template_name = 'causes_maladie/cause_maladie_list.html'
    context_object_name = 'causes_maladie'

# Detail view for Cause Maladie
class CauseMaladieDetailView(DetailView):
    model = CauseMaladie
    template_name = 'causes_maladie/cause_maladie_detail.html'
    context_object_name = 'cause_maladie'

# Create view for Cause Maladie
class CauseMaladieCreateView(CreateView):
    model = CauseMaladie
    fields = ['nom', 'description', 'type']
    template_name = 'causes_maladie/cause_maladie_form.html'
    success_url = reverse_lazy('cause_maladie-list')

# Update view for Cause Maladie
class CauseMaladieUpdateView(UpdateView):
    model = CauseMaladie
    fields = ['nom', 'description', 'type']
    template_name = 'causes_maladie/cause_maladie_form.html'
    success_url = reverse_lazy('cause_maladie-list')

# Delete view for Cause Maladie
class CauseMaladieDeleteView(DeleteView):
    model = CauseMaladie
    template_name = 'causes_maladie/cause_maladie_confirm_delete.html'
    success_url = reverse_lazy('cause_maladie-list')
