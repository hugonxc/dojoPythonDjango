from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

class Operacoes(object):
    """docstring for Operacoes."""

    def adicao(self, firstValue, secondValue):
        result = firstValue + secondValue
        return result



# Create your views here.
class Calculadora(object):
    """docstring for Calculadora."""

    def calculadoraPage(request):
        print("HELLO DARKNESS")
        operador = Operacoes()
        result = 0;
        context = {}

        print("conteudo da request",request.GET)
        if(request.GET):
            firstValue = int(request.GET['firstValue'])
            secondValue = int(request.GET['secondValue'])
            result = operador.adicao(firstValue, secondValue)
            context = {"resultado": result}

        arr = [1,4,9,16,25,36]
        context = {"vetor": arr}
        return render(request, 'calculadora.html', context)




class BokehViz(object):
    """docstring for BokehViz."""

    def simple_chart(request):
        arr = [1,4,9,16,25,36]
        y = [1,2,3,4,5,6]
        plot = figure()
        plot.line(arr, y)

        script, div = components(plot, CDN)
        return render(request, "example.html", {"script": script, "div":div})
