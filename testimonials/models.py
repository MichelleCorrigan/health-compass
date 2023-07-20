from django.db import models


class Testimonial(models.Model):
    review = models.TextField()
    name = models.CharField(max_length=50)
    date = models.DateField(help_text='yyyy-mm-dd')

    def __str__(self):
        return self.review
