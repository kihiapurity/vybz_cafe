# VybzCafeProject\cafewebsite\models.py
from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MenuItemImage(models.Model):
    menu_item = models.ForeignKey('Menu', related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.menu_item.name}"


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Use ForeignKey for category

    def __str__(self):
        return self.name

    def get_all_images(self):
        return self.images.all()


class Update(models.Model):
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField()

class HomePageSettings(models.Model):
    brand_logo = CloudinaryField('image')
    brand_name = models.CharField(max_length=255)
    twinkling_text = models.CharField(max_length=255)
    welcome_message = models.TextField()

    def __str__(self):
        return self.brand_name + " - Home Page Settings"
