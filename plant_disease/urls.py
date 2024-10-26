from django.urls import path
from . import views
from  plant_disease.view import TypeView, plantView, MaladieView, causeView 
from .views import dashboard_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('predict/', views.predict, name='predict'),  # Predict page URL
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('backoffice/', views.backoffice_view, name='backoffice'),
    # *************

    path('typePlantes/', TypeView.TypePlanteListView.as_view(), name='typePlantes-list'),
    path('typePlantes/<int:pk>/', TypeView.TypePlanteDetailView.as_view(), name='typePlantes-detail'),
    path('typePlantes/create/', TypeView.TypePlanteCreateView.as_view(), name='typePlantes-create'),
    path('typePlantes/<int:pk>/update/', TypeView.TypePlanteUpdateView.as_view(), name='typePlantes-update'),
    path('typePlantes/<int:pk>/delete/', TypeView.TypePlanteDeleteView.as_view(), name='typePlantes-delete'),

    #**********************
    path('plantes/', plantView.PlanteListView.as_view(), name='plante-list'),
    path('plantes/<int:pk>/', plantView.PlanteDetailView.as_view(), name='plante-detail'),
    path('plantes/create/', plantView.PlanteCreateView.as_view(), name='plante-create'),
    path('plantes/<int:pk>/update/', plantView.PlanteUpdateView.as_view(), name='plante-update'),
    path('plantes/<int:pk>/delete/', plantView.PlanteDeleteView.as_view(), name='plante-delete'),
    

      # Maladie URLs
    path('maladies/', MaladieView.MaladieListView.as_view(), name='maladie-list'),
    path('maladies/<int:pk>/', MaladieView.MaladieDetailView.as_view(), name='maladie-detail'),
    path('maladies/create/', MaladieView.MaladieCreateView.as_view(), name='maladie-create'),
    path('maladies/<int:pk>/update/', MaladieView.MaladieUpdateView.as_view(), name='maladie-update'),
    path('maladies/<int:pk>/delete/', MaladieView.MaladieDeleteView.as_view(), name='maladie-delete'),
    path('maladies/', MaladieView.MaladieListView.as_view(), name='maladie-list'),

      # Cause URLs

     path('causes_maladie/', causeView.CauseMaladieListView.as_view(), name='cause_maladie-list'),
    path('causes_maladie/<int:pk>/', causeView.CauseMaladieDetailView.as_view(), name='cause_maladie-detail'),
    path('causes_maladie/create/', causeView.CauseMaladieCreateView.as_view(), name='cause_maladie-create'),
    path('causes_maladie/<int:pk>/update/', causeView.CauseMaladieUpdateView.as_view(), name='cause_maladie-update'),
    path('causes_maladie/<int:pk>/delete/', causeView.CauseMaladieDeleteView.as_view(), name='cause_maladie-delete'),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    