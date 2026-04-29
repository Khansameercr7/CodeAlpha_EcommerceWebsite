from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name', 'price', 'stock', 'available', 'category', 'image_url_preview']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_filter   = ['available', 'category']
    search_fields = ['name']
    readonly_fields = ['image_url_preview']
    fieldsets = (
        ('Product Info', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock', 'available')
        }),
        ('Images', {
            'fields': ('image', 'image_url', 'image_url_preview')
        }),
    )

    def image_url_preview(self, obj):
        if obj.image_url:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image_url)
        return "No image URL"
    image_url_preview.short_description = "Image Preview"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}