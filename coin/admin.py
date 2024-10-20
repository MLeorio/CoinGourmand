from django.contrib import admin
from .models import Product, Category

# Register your models here.


admin.site.site_header = "Administration de Coin Gourmand"
admin.site.site_title = "Admin Coin Gourmand"
admin.site.index_title = "Bienvenu dans l'interface d'administration"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'description', 'created_at')
    search_fields = ('label', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'created_at', 'updated_at')
    search_fields = ('name',)