from django.db import models
from django.urls import reverse

class Menu(models.Model):

	name= models.CharField('Name', max_length=100)
	slug = models.SlugField('URL', max_length=100)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	kids = models.ManyToManyField('self', blank=True)

	def get_absolute_url(self):
		return reverse('menu_detail', kwargs={'menu_slug': self.slug})

	class Meta:
		verbose_name = 'Menu'
		verbose_name_plural = 'Menu'

	def __str__(self):
		return self.name
