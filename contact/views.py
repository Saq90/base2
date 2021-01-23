from django.shortcuts import render,redirect

from .models import Contact
def home(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address', '')
        contact = Contact(name=name, email=email, phone=phone,address=address)
        contact.save()
        return redirect('/')
    return render(request, "contact.html")