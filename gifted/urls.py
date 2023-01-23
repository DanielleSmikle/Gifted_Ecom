from django.urls import path 
from . import views 

app_name= 'gifted'

urlpatterns = [
    path('', views.feature_all, name='feature_all'),
    path('<slug:slug>', views.feature_detail, name= 'feature_detail'),
    path('shop/<slug:collection_slug>/', views.collection_list, name='collection_list'),
]


