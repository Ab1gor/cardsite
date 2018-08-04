from django.urls import path, include
from . import views
from .views import CardSerializerView

urlpatterns = [
    #path('signup/',views.SignUp.as_view(),name='signup'),
    #path('login/',views.login1,name='login'),
    path('card/',CardSerializerView.as_view(), name='apicard'),
]