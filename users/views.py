from django.shortcuts import render
from users.forms import UserRegistrationForm

# Create your views here.
def register(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"users/register.html",context)
