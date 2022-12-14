from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Evento
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from .forms import Asistir
from pyexpat.errors import messages


def perfil(request):
	template_name = 'perfil.html'
	eventos = Evento.objects.all()

	ctx = {
		'eventos': eventos
	}
	
	return render(request, template_name, ctx)


class Listar(ListView):
	template_name = 'perfil.html'
	model=Evento
	paginate_by = 1
	context_object_name = "eventos"

	def get_queryset(self):
		return Evento.objects.all().order_by("fecha")

"""class Crear(LoginRequiredMixin, SuperUserRequiredMixin, CreateView):
    model = Evento
    form_class = EquipoForm
    template_name = "equipos/crear.html"

    def get_success_url(self, **kwargs):
        return reverse('equipos:listar')"""



"""def eliminar(request, id_evento):
	evento = Evento.objects.get(pk = id_evento)
	ctx= {
		'eventos': Evento.objects.get(pk = id_evento)
	}
	evento.delete()

	render (request, 'perfil.html', ctx)"""

def listarEventos(request):
	template_name = 'eventos/listaEvento.html'
	form = Asistir(initial={'id_id_Usuario':'mercadillo@mail.com', 'id_Evento':'s'})
	print('formmmmmmmm', form)
	eventos = Evento.objects.all().values('id_evento','titulo', 'categoria')
	
	print(eventos) 

	if request.method =="POST":
		#asistencia = Asistencia(id_Evento=)
		form = Asistir(request.POST)
		# form.id_Usuario = get_object_or_404(Usuario, pk=request.user.pk)
		# form.id_Evento = request.POST.get('event_id')
		# print('id eventoooooooo', request.POST.get('event_id'))
		# print('formmmmmmmmmm', form.id_Usuario)
		if form.is_valid():
			form.save()

	ctx = {
		'eventos': eventos,
		'form':form
	}
	print('contextoo', ctx)
	return render (request, template_name, ctx)