from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
#
# Create your models here.
class Event(models.Model):
	event_name = models.CharField(max_length=100)
	event_desc = models.TextField()
#Not sure if this is needed yet	date_posted = models.DateTimeField(default=timezone.now)
	start_date = models.DateTimeField(default=timezone.now)
	end_date   = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=100,unique=True)
#
	def __str__(self):
		return self.event_name
#
def unique_slug_generator(model_instance, event_name, slug_field):
	slug = slugify(event_name)
	model_class = model_instance.__class__
	# Event.objects.filter(slug=slug).exists()
# In case multiple people use the same event_name, increment their url
	while model_class._default_manager.filter(slug=slug).exists():
		#if it exists get the last primary key
		object_pk = model_class._default_manager.latest('pk')
		object_pk = object_pk.pk + 1
		#returns full object the last primary key, retrieve primary key, then increment it
		slug = f'{slug}-{object_pk}'
	return slug
    #
def slug_save(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance, instance.event_name, instance.slug)
pre_save.connect(slug_save, sender=Event)
