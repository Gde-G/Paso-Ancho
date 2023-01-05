from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

from .forms import ConsultaForm
from .models import Consulta

# Suplementary path for id tags

context = {
    'cabaña8': 'cabañas#8personas',
    'actividades0': 'actividades#senderismo',
    'actividades1': 'actividades#trekking',
    'actividades2': 'actividades#algo',
    'actividades3': 'actividades#diacampo',
    'form': ConsultaForm()
}

# Create your views here.


def home(request: HttpRequest):

    return render(request, 'base/home.html', context=context)


def cabañas(request: HttpRequest):

    return render(request, 'base/cabañas.html', context=context)


def alrededores(request: HttpRequest):

    return render(request, 'base/alrededores.html', context=context)


def actividades(request: HttpRequest):

    return render(request, 'base/actividades.html', context=context)


def galeria(request: HttpRequest):

    return render(request, 'base/galeria.html', context=context)


def contactanos(request: HttpRequest):

    return render(request, 'base/contactanos.html', context=context)


def consulta(request: HttpRequest):
    form = ConsultaForm()

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
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
            except:
                messages.error(
                    request, 'La consulta NO fue enviada debido a un error. Recuerde completar todos los campos y el Captcha!')
            return redirect(request.META['HTTP_REFERER'])
        else:
            print(form)
            for field, errors in form.errors.items():
                if field == "captcha" and errors[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                messages.error(request, f"ERROR in {field}... {errors}" )
            return redirect(request.META['HTTP_REFERER'])