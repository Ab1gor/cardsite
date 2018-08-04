from django.shortcuts import render, redirect, get_list_or_404
from .models import carddetails
from .forms import carddetailsForm, addcommentForm , SignUpForm
from django.utils import timezone
from django.views.decorators.http import require_POST
from comment.models import commentcount, Reply
from likes.models import likecount
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


def carddetails_details_view(request, id=1):
	queryset = carddetails.objects.all().values('model_pic','user_id', 'user' ,'title','description','id', 'pub_date','private')
	
	b = request.user


	for index,query in enumerate(queryset):
		queryset[index]['comment'] = commentcount.objects.filter(card_id=query['id'])	
		queryset[index]['likes'] = likecount.objects.filter(card_id=query['id'])
		flag=0
		queryset[index]['status']="Like"
		queryset[index]['count'] = 0
		for lik in query['likes']:
			for li in lik.user.all():
			#print(lik.user)
			    if li == b:
			#print("YES")
				    queryset[index]['status']="Unlike"
				#print(queryset[index]['status'])
				    flag = 1
			#print(queryset[index]['status'])
			queryset[index]['count'] = lik.user.all().count()

	
	#import ipdb;ipdb.set_trace()


	#for query in queryset['likes']:
		#print(query)

	form = carddetailsForm()
	form1 = addcommentForm()
	 


	

	

	context = {
	"object" : queryset,
	"form" : form,
	"comment" : form1,
	#"comment" :querysetcomment,
	}
	return render(request, "home.html", context)

@require_POST
def addcard(request):
	form = carddetailsForm(request.POST,request.FILES)

	#import ipdb;ipdb.set_trace()
	data = request.POST.dict()
	if form.is_valid():
		card = carddetails()
		card.model_pic = request.FILES['file']
		card.title = data['title']
		card.description 	= 	data['description']
		card.user = request.user
		card.pub_date = timezone.now()
		card.save()
	return redirect('addcard')



@require_POST
def addcomment(request):
	form = addcommentForm(request.POST)
	#queryset = carddetails.objects.get(request)
	#print(queryset)
	data = request.POST.dict()
	#import ipdb; ipdb.set_trace()

	if form.is_valid():
		comment = commentcount()
		comment.user = request.user
		comment.usercomment =  data['title']
		comment.card = carddetails.objects.filter(id=data['card_id'])[0]
		comment.save()
	return redirect('addcard')


@require_POST
def addlike(request):
	data = request.POST.dict()
	check= data['like_status']



	if check == "Like":
	    #import ipdb;ipdb.set_trace()
	    try:
	    	likes=likecount.objects.filter(card_id=data['card_id'])[0]
	    	likes.user.add(request.user)
	    except:
	    	likes = likecount()
	    	likes.card = carddetails.objects.filter(id=data['card_id'])[0]
	    	likes.save()
	    	likes.user.add(request.user)
	else:
		#import ipdb;ipdb.set_trace()
		likes=likecount.objects.filter(card_id=data['card_id'])[0]
		likes.user.remove(request.user)
		

	return redirect('addcard')


@require_POST
def search(request):
	data =request.POST.dict()
	#import ipdb;ipdb.set_trace()
	queryset = carddetails.objects.filter(title__contains=data['search']).values('model_pic','user_id', 'user' ,'title','description','id', 'pub_date','private')
	
	b = request.user


	for index,query in enumerate(queryset):
		queryset[index]['comment'] = commentcount.objects.filter(card_id=query['id'])	
		queryset[index]['likes'] = likecount.objects.filter(card_id=query['id'])
		flag=0
		queryset[index]['status']="Like"
		queryset[index]['count'] = 0
		for lik in query['likes']:
			for li in lik.user.all():
			#print(lik.user)
			    if li == b:
			#print("YES")
				    queryset[index]['status']="Unlike"
				#print(queryset[index]['status'])
				    flag = 1
			#print(queryset[index]['status'])
			queryset[index]['count'] = lik.user.all().count()
	
	#import ipdb;ipdb.set_trace()


	#for query in queryset['likes']:
		#print(query)

	form = carddetailsForm()
	form1 = addcommentForm()
	 


	

	

	context = {
	"object" : queryset,
	"form" : form,
	"comment" : form1,
	#"comment" :querysetcomment,
	}
	return render(request, "home.html", context)

@require_POST
def reply(request):
	data = request.POST.dict()
	a = Reply()
	#import ipdb;ipdb.set_trace()
	a.text = data['reply1']
	s = data['reply1']
	a.user = request.user
	a.save()
	b= commentcount()
	b = commentcount.objects.filter(id=int(data['comment_id']))[0]
	b.save()
	b.reply.add(a)
	return redirect('addcard')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


























