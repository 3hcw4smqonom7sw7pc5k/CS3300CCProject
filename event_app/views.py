from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Event
from .forms import EventForm, CreateUserForm
from django.template import loader
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin
#https://www.w3schools.com/django/django_add_record.php
# Create your views here.
def index(request):
	return render( request, 'event_app/index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['editor_role'])
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
class EventListView(LoginRequiredMixin, ListView):
	model = Event
class EventDetailView(LoginRequiredMixin, DetailView):
	model = Event

@login_required(login_url='login')
@allowed_users(allowed_roles=['editor_role'])
def EventUpdate(request, pk):
	event = Event.objects.get(pk=pk)
	if request.method == 'POST':
		form = EventForm(request.POST, instance=event)
		form.save()
		return redirect('event-detail', pk=pk)
	else:
		form = EventForm(instance=event)
	return render(request, "event_app/event_form.html", {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['editor_role'])
def EventDelete(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    else:
        return render(request, 'event_app/event_confirm_delete.html', {'event':event})

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            #Reader or Editor here, so even users can view, but not edit based on their group
            Group.objects.create(name='reader')
            group = Group.objects.get(name='reader')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
            
    context={'form':form}
    return render(request, 'registration/register.html', context)
