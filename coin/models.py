from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Prix')
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ajouter le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifer le")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-created_at']

