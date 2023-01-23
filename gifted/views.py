from django.shortcuts import get_object_or_404, render

from .models import Collection, Feature

def feature_all(request): 
    features = Feature.features.all()
    return render(request, 'gifted/home.html', {'features': features})

def feature_detail(request, slug):
    feature = get_object_or_404(Feature, slug=slug, in_stock=True)
    return render(request, 'gifted/features/single.html', {'feature' : feature})

def collection_list(request, collection_slug):
    collection = get_object_or_404(Collection, slug=collection_slug)
    features = Feature.objects.filter(collection=collection)
    return render(request, 'gifted/features/collection.html', {'collection': collection, 'features':features})


