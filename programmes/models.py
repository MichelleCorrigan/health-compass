from django.db import models


class Programme(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
