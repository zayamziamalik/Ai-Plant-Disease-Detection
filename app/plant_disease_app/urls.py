from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from .views import home

urlpatterns = [
    path('', home, name='home'),

]