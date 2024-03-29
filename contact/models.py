from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Message'
