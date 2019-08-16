from django.db import models
from django.shortcuts import reverse

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_detail', args=[str(self.id)])


class Street(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    length = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.name, self.length)

    def get_absolute_url(self):
        return reverse('street_detail', args=[str(self.id)])
