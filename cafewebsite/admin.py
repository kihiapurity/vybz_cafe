# VybzCafeProject\cafewebsite\admin.py
from django.contrib import admin
from .models import Category, Menu, Update, HomePageSettings, MenuItemImage

class MenuItemImageInline(admin.TabularInline):
    model = MenuItemImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_display_links = ('name',)
    inlines = [MenuItemImageInline]  # Add inline editing for images

    def get_ordering(self, request):
        return ['category', 'name']  # Order by category then by name

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('price', 'description')

@admin.register(HomePageSettings)
class HomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)

admin.site.site_header = "Vybz Cafe Admin"
admin.site.site_title = "Vybz Cafe Admin"
admin.site.index_title = "Site Administration"
