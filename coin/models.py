from django.db import models

# Create your models here.

class Category(models.Model):
    label = models.CharField(max_length=200, verbose_name="Libellé de la catégorie", unique=True)
    description = models.TextField(verbose_name="Description...", null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ajouter le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifer le")
    
    def __str__(self):
        return self.label
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["-created_at"]

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Prix')
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ajouter le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifer le")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-created_at']

