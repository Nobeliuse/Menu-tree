from django.urls import path
from .views import Home


urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('menu/<slug:menu_slug>', Home.as_view(), name='menu_detail')
]