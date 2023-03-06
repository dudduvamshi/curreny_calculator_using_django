from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
 #   return HttpResponse("<h1>Hello world..</h1>")
    return render (request, 'index.html')


CurrencyRates = {'AUD':55.55,'USD':82.23}


def convert(request):
    if request.method == 'POST':
        v1 = request.post.get('cur_from')
        v2 = request.post.get('amount')
        v3 = request.post.get('cur_to')

        CurrencyRates = {
            'AUD':55.55,
            'USD':82.23,
            'DKK':11.73,
            'JPY':0.60,
            'CAD':60.14,
            'CNY':11.14,
            'CZK':3.71,
            'EUR':87.05,
            'GBP':98.42,
            'NOK':4.82,
            'NZD':50.81,
        }

        val1 = CurrencyRates[v1]
        val2 = CurrencyRates[v3]
        convert1 = val1/val2
        convert = round((v2 * convert1),2)
        print ("From :", v1, v2, "\n", "To :", v3, convert)
            
        return render ('index')