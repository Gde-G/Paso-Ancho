from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

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


def galeria(request: HttpRequest):
    contexto = {
        'cabaña8': caba[0],
        'actividades0': activi[0], 
        'actividades1': activi[1],
        'actividades2': activi[2],
        'actividades3': activi[3]
    }
    return render(request, 'base/galeria.html', context=contexto)


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
        name = request.POST.__getitem__('name'),
        email = request.POST.__getitem__('email'),
        date_from = request.POST.__getitem__('date_from'),
        date_to = request.POST.__getitem__('date_to'),
        amount_adults = request.POST.__getitem__('amount_adults'),
        amount_kids = request.POST.__getitem__('amount_kids'),
        question = request.POST.__getitem__('question')

        context = {
            'name': name[0],
            'email': email[0],
            'date_from': date_from[0], 
            'date_to': date_to[0], 
            'amount_adults': amount_adults[0], 
            'amount_kids': amount_kids[0],
            'question': question, 
        }

        temp = get_template('base/email_template.html')

        content = temp.render(context)

        corr = EmailMultiAlternatives(
            subject='Consulta desde pasoanchova.com',
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=email)
        
        corr.attach_alternative(content, 'text/html')
        corr.send(fail_silently=False)
        
        
        messages.success(request, 'La consulta fue enviada exitosamente!')
        
        con = Consulta.objects.create( 
            name=name,
            email=email,
            question=question
            )
        
        return redirect(request.META['HTTP_REFERER'])