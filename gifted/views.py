from django.shortcuts import render

from .models import Collection, Feature

def all_features(request):
    features = Feature.objects.all()
    return render(request, 'gifted/home.html', {'features': features})




