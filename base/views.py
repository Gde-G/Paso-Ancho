from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

from .forms import ConsultaForm
from .models import Consulta

#Suplementary path for id tags 
activi = ['actividades#senderismo',
          'actividades#trekking',
          'actividades#algo',
          'actividades#diacampo']

caba = ['cabañas#8personas']


# Create your views here.
def home(request:HttpRequest):
    

    contexto = {
        'cabaña8': caba[0],
        'actividades0': activi[0], 
        'actividades1': activi[1],
        'actividades2': activi[2],
        'actividades3': activi[3]
    }
    return render(request, 'base/home.html', contexto)


def cabañas(request: HttpRequest):
    
    contexto = {
        'cabaña8': caba[0],
        'actividades0': activi[0], 
        'actividades1': activi[1],
        'actividades2': activi[2],
        'actividades3': activi[3]
    }
    return render(request, 'base/cabañas.html', contexto)


def alrededores(request: HttpRequest):

    contexto = {
        'cabaña8': caba[0],
        'actividades0': activi[0], 
        'actividades1': activi[1],
        'actividades2': activi[2],
        'actividades3': activi[3]
    }
    return render(request, 'base/alrededores.html', contexto)


def actividades(request: HttpRequest):
    
    
    contexto = {
        'cabaña8': caba[0],
        'actividades0': activi[0], 
        'actividades1': activi[1],
        'actividades2': activi[2],
        'actividades3': activi[3]
    }
    return render(request, 'base/actividades.html', contexto)


def contactanos(request: HttpRequest):
    
    
    contexto = {
        'cabaña8': caba[0],
        'actividades0': activi[0], 
        'actividades1': activi[1],
        'actividades2': activi[2],
        'actividades3': activi[3]
    }
    return render(request, 'base/contactanos.html', contexto)


def consulta(request: HttpRequest):
    form = ConsultaForm()
    
    if request.method == 'POST':
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        question = request.POST.get('question')
        
        body = f'''Consulta:\n\nNombre: {name}\nMail: {email}\nPregunta: {question}'''

        email = EmailMessage(
            subject='Consulta desde la pagina Web',
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER]
        )
        
        email.send(fail_silently=False)

        messages.success(request, 'La consulta fue enviada exitosamente!')
        
        con = Consulta.objects.create( 
            name=name,
            email=email,
            question=question
            )
        
        return redirect(request.META['HTTP_REFERER'])