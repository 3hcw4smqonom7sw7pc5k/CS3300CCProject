from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Event
#
# Create your views here.
def index(request):
    return render( request, 'event_app/index.html')
class EventListView(generic.ListView):
    model = Event
class EventDetailView(generic.DetailView):
    model = Event