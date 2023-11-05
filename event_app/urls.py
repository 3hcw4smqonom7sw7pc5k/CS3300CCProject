from django.urls import path
from . import views
#
urlpatterns = [
		path('', views.index, name='index'),
		path('events/', views.EventListView.as_view(), name= 'events'),
		path('event/<int:pk>', views.EventDetailView.as_view(), name= 'event-detail'),
		path('event/create_event/', views.eventCreate, name='event_create'),
		path('event/<int:pk>/update/', views.EventUpdate, name= 'event_update'),
		path('event/<int:pk>/delete/', views.EventDelete, name= 'event_delete'),
		]