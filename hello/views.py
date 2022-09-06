from django.shortcuts import render
from django.http import HttpResponse
from hello import script1

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    try:
        script1.PublicarTweet("Preferiría no hacerlo3")
        return render(request, "index.html")
    except ValueError:
        print("FALLO")
    
    


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
