from django.conf.urls import url
from .views import Calculadora, BokehViz

urlpatterns = [
    url(r'^$', Calculadora.calculadoraPage),
    url(r'^bokehViz$', BokehViz.simple_chart),    
]
