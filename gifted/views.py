from django.shortcuts import render, get_object_or_404

from .models import Collection, Feature



# collecting all the colletion information 
def collections(request):
    return{
        'collections': Collection.objects.all()
    }
# getting all the data, from features select all  
def all_features(request): 
    features = Feature.objects.all()
    return render(request, 'gifted/home.html', {'features': features})
#making indvi page for each product 
def feature_detail(request, slug):
    feature = get_object_or_404(Feature, slug=slug, in_stock=True)
    return render(request, 'gifted/features/detail.html', {'feature': feature})

def collection_list(request, collection_slug):
    collection = get_object_or_404(Collection, slug=collection_slug)
    features = Feature.objects.filter(collection=collection)
    return render(request, 'gifted/features/collection.html', {'collection': collection, 'features':features})
