from django.urls import path 
from . import views 

app_name= 'gifted'

urlpatterns =[
    path('', views.all_features, name='all_features'),

]

