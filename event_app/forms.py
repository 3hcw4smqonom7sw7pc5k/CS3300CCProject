from django.forms import ModelForm
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =('event_name', 'event_desc', 'start_date', 'end_date')

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
