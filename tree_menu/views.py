from django.shortcuts import render
from django.views import View
from .models import Menu

class Home(View):

	template_name = 'tree_menu/main.html'

	def get(self, request, menu_slug=None):
		context = {
			'title': 'Home',
			'selected': menu_slug,
		}
		return render(request, self.template_name, context=context)