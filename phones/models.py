from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

