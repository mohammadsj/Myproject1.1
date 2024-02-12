from django.urls import path
from mysite.views import *

app_name = 'mysite'
urlpatterns = [
    path('',home_view,name='home')
    
    
]