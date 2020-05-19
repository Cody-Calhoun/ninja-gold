from django.shortcuts import render, HttpResponse , redirect
import random

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    
    return render (request, "index.html")

def process_money(request):

    building = request.POST['building']
    if building == "farm":
        request.session['gold'] += random.randint(10, 20)
    elif building == "cave":
        request.session['gold'] += random.randint(5, 10)
    elif building == "house":
        request.session['gold'] += random.randint(2, 5)
    elif building == "casino":
        request.session['gold'] += random.randint(-50, 50)    
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")