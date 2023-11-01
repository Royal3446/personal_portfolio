from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('Phoneno')
        fdescription = request.POST.get('description')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdescription)
        query.save()
        messages.success(request,'Thanks for contacting us. we will get by you soon')
        return redirect('/contact')
        
    return render(request,'contact.html')

def skill(request):
    return render(request,'skill.html')


def project(request):
    return render(request,'project.html')

def resume(request):
    return render(request,'resume.html')
