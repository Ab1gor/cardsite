from django.urls import path, include
from . import views
from .views import carddetails_details_view, addcard, addcomment, addlike,search, reply , signup

urlpatterns = [
    #path('signup/',views.SignUp.as_view(),name='signup'),
    #path('login/',views.login1,name='login'),
    path('',views.carddetails_details_view, name='addcard'),
    path('addcard',views.addcard, name='savecard'),
    path('addcomment', views.addcomment, name= 'addcomment'),
    path('addlike',views.addlike, name= 'addlike'),
    path('search',views.search, name= 'search'),
    path('reply',views.reply, name= 'reply'),
    path('signup',views.signup, name = 'signup'),
    path('api/',include('card.api.urls'),name='api'),

]