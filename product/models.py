from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.name