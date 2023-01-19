from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'funny/home.html')


def contacts(request):
    if request.method =="POST":
        print(request.POST.get("name"))
        print(request.POST.get("phone"))
        print(request.POST.get("message"))
    return render(request,'funny/contacts.html')