from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    #path('login/',views.login1,name='login'),
    path('home/',views.home, name='home1'),
    path('edit/',views.updatedetails1, name='edit'),
    path('updated/', views.updatedetails, name = 'update')
]