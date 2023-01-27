from django.shortcuts import render, get_object_or_404

from .models import Collection, Feature



# collecting all the colletion information 

# getting all the data, from features select all  
def feature_all(request): 
    features = Feature.features.all()
    return render(request, 'gifted/home.html', {'features': features})


#making indvi page for each product 
def feature_detail(request, slug):  #name chage is not needed, shows the detail of the product while showing for a single product
    feature = get_object_or_404(Feature, slug=slug, in_stock=True)
    return render(request, 'gifted/features/single.html', {'feature': feature})

def collection_list(request, collection_slug):
    collection = get_object_or_404(Collection, slug=collection_slug)
    features = Feature.objects.filter(collection=collection)
    return render(request, 'gifted/features/collection.html', {'collection': collection, 'features':features})
