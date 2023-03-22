from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('application', views.application, name='application'),
    path('vac-honeymoon-application', views.vac_hm_application, name='vac_hm'),
    path('services/honeymoon', views.honeymoon, name="honeymoon"),
    path('services/chauffeur', views.chauffeur, name='chauffeur'),
    path('services/nursing_opportunities_and_internships', views.internship, name='internship'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
