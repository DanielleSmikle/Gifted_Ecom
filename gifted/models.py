from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#will only produce data that is acrive/ avaiable 
class FeatureManager(models.Manager):
    def get_queryset(self):
        return super(FeatureManager, self).get_queryset().filter(is_active=True)


class Collection(models.Model):
    name= models.CharField(max_length =255, db_index = True)
    slug = models.SlugField(max_length=255, unique=True, default='collection')

    class Meta:
        verbose_name_plural = 'collections'

    def get_absolute_url(self):
        return reverse('gifted:collection_list', args=[self.slug])
 
    def __str__(self):
        return self.name


SIZE_CHOICES = (
    ('small', 'SMALL'),
    ('large', 'LARGE')
)

class Feature(models.Model):
    collection = models.ForeignKey(Collection, related_name='feature', on_delete=models.CASCADE)
    scent = models.CharField(max_length =255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, default='features')
    size = models.CharField(max_length=5, choices= SIZE_CHOICES, default='small')
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    features = FeatureManager()
    

    class Meta:
        verbose_name_plural= 'Features'
        ordering=('-created', )

    def get_absolute_url(self):
        return reverse('gifted:feature_detail', args=[self.slug])

    def __str__(self):
        return self.scent






