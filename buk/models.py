from django.db import models
from django.contrib.gis.db import models
from django.urls import reverse
from django.db import transaction


# Create your models here.


class road(models.Model):
    state_code = models.CharField(max_length=254, null='False')
    source = models.CharField(max_length=254, null='False')
    name = models.CharField(max_length=254, null='False')
    surface_ty = models.CharField(max_length=254, null='False')
    smoothness = models.CharField(max_length=254, null='False')
    one_way = models.IntegerField()
    osm_class = models.CharField(max_length=254, null='False')
    road_class = models.CharField(max_length=254, null='False')
    global_id = models.CharField(max_length=254, null='False')
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return 'Name: %s' % self.name

class places(models.Model):
    objectid = models.BigIntegerField()
    state_code = models.CharField(max_length=254, null='False')
    source = models.CharField(max_length=254, null='False')
    name = models.CharField(max_length=254, null='False')
    alt_name = models.CharField(max_length=254, null='False')
    ward_code = models.CharField(max_length=254, null='False')
    is_primary = models.IntegerField()
    global_id = models.CharField(max_length=254, null='False')
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return 'Name: %s' % self.name


    def save(self, *args, **kwargs): # < here
        self.slug = slugify(self.name)
        super(Places, self).save()

    def get_absolute_url(self): # < here
        return reverse('detail', args=[str(self.name)])


class boundary(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return 'Name: %s' % self.id





    #def __str__(self):
        #return self.surface_ty

    #def __unicode__(self):
        #return self.source

    #class Meta:
       #verbose_name = "road"
