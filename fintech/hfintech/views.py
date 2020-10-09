from django.shortcuts import render,redirect,HttpResponse


from json import dumps


# Create your views here.


def index(request):
    dataDictionary = {'Passing Data': 'From Python to JS', 
    'geeks': 'forgeeks', 'ABC': 123, 456: 'abc', 
    14000605: 1, 'list': ['geeks', 4, 'geeks'], 
     }
    # dump data 
    dataJSON = dumps(dataDictionary)
    return render(request,'index.html',{'data':dataJSON})
