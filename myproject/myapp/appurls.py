from django.urls import path
from myapp import views

urlpatterns = [
    path('personas', views.personas, name="personas-url"),
    path('personaCrear', views.personaCrear, name="personaCrear-url"),
    path('personaEditar/<int:id>/', views.personaEditar , name="personaEditar-url"),
    path('personaActualizar/<int:id>/', views.personaActualizar, name="personaActualizar-url"),
    path('personaBorrar/<int:id>/', views.personaBorrar, name="personaBorrar-url"),
    #path('personaDetalle', views.personaDetalle, name="personaDetalle-url"),
]