from django.urls import path
from . import views
from django.conf.urls import include
#
urlpatterns = [
		#user accounts
#20231128
# in django urls.py now		path('accounts/', include('django.contrib.auth.urls')),
#		path('accounts/register/', views.registerPage, name='register_page'),
		path('', views.index, name='index'),
		path('events/', views.EventListView.as_view(), name= 'events'),
		path('event/<int:pk>', views.EventDetailView.as_view(), name= 'event-detail'),
		path('event/create_event/', views.eventCreate, name='event_create'),
		path('event/<int:pk>/update/', views.EventUpdate, name= 'event_update'),
		path('event/<int:pk>/delete/', views.EventDelete, name= 'event_delete'),
		path('logout', views.logout_view)
		]
