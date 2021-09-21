import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.entrada.models import Entry
from .models import Home
from .forms import ContactForm, SuscribersForm





from django.views.generic import (
    TemplateView,
    CreateView
)



class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #cargamos el home
        context['home'] = Home.objects.latest('created')
        #contexto de portada
        context['portada'] = Entry.objects.entrada_portada()
        #contexto para los articulos del home
        context['entrada_home'] = Entry.objects.entrada_home()
        #contexto para las entradas recientes
        context['entrada_reciente'] = Entry.objects.entrada_reciente()
        #enviamos formulario de suscripcion
        context['suscripcion']  = SuscribersForm
        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
