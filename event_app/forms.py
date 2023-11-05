from django.forms import ModelForm
from .models import Event
#
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =('event_name', 'event_desc', 'start_date', 'end_date')
