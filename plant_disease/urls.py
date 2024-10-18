from django.urls import path
from . import views
from  plant_disease.view import TypeView, plantView
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
    
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    