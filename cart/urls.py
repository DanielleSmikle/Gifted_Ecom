from django.urls import path 
from . import views

urlpatterns =[
    path('admin/', views.cart_summary, name ='cart_summary')
    

]