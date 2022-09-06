from django.shortcuts import render
from django.http import HttpResponse
from hello import script1

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()
    script1.PublicarTweet("Preferiría no hacerlo")

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
