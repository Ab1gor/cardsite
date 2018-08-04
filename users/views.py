from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import userdetails
from django.contrib.auth.models import User
from .forms import userdetailsForm
from django.views.decorators.http import require_POST
# Create your views here.


class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'





def home(request):
    
    return render(request, 'home.html')



def updatedetails1(request):
    form = userdetailsForm()
    queryset = userdetails.objects.filter(user=request.user)
    for a in queryset:
        print(a.about)
    context = {
    "form" : form,
    "user1" : queryset,
    }
    return render(request, 'editdetails.html', context)

@require_POST
def updatedetails(request):
    form = userdetailsForm(request.POST)  
    data = request.POST.dict()
    print(data)
    user = userdetails()
    user.about = data['about']
    user.url  =  data['url']
    user.company  =  data['company']
    user.user = request.user
    user.save()
    return render(request, 'back.html')

