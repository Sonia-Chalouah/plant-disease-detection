from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  plant_disease.Model.typePlant import TypePlante
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import google.generativeai as genai
import json


# Set up the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def ai_generate_description(nom):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"generate a detailed description in 4 lines for: {nom}"
    response = model.generate_content(prompt)
    return response.text
@csrf_exempt
def generate_description(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nom = data.get('nom', '')
            description = ai_generate_description(nom)
            return JsonResponse({'description': description})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid Request'}, status=400)


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
    success_url = '/typePlantes/'


# Mettre à jour un type de plante (Update)
class TypePlanteUpdateView(UpdateView):
    model = TypePlante
    fields = ['nom', 'description', 'image']
    template_name = 'type_plante/typeplante_form.html'
    success_url = '/typePlantes/'


# Supprimer un type de plante (Delete)
class TypePlanteDeleteView(DeleteView):
    model = TypePlante
    template_name = 'type_plante/typeplante_confirm_delete.html'
    success_url = '/typePlantes/'



