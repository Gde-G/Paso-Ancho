from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),

    path("cabañas/", views.cabañas, name='cabañas'),
    path("cabañas/8personas", views.cabañas, name='cabañas8'),

    path("alrededores/", views.alrededores, name='alrededores'),

    path("actividades/", views.actividades, name='actividades'),
    path("actividades/senderismo", views.actividades, name='actividades0'),
    path("actividades/trekking", views.actividades, name='actividades1'),
    path("actividades/algo", views.actividades, name='actividades2'),
    path("actividades/diacampo", views.actividades, name='actividades3'),

    path("contactanos/", views.contactanos, name='contactanos'),

    path("consulta/", views.consulta, name='consulta')

]