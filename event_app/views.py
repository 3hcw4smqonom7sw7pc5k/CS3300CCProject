from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Event
from .forms import EventForm
from django.template import loader
#https://www.w3schools.com/django/django_add_record.php
# Create your views here.
def index(request):
	return render( request, 'event_app/index.html')
def eventCreate(request):
	form = EventForm()
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			event = form.save(commit=False)
			event.save()
			return redirect('event-detail', event.id)
			
	context = {'form': form}
	return render(request, 'event_app/event_form.html', context)
class EventListView(ListView):
	model = Event
class EventDetailView(DetailView):
	model = Event