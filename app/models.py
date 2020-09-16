from django.db import models

class Record(models. Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=12)
    whatsapp = models.CharField(max_length=12)

    def __str__(self):
        return self.name