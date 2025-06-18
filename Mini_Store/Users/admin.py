from django.contrib import admin
from .models import User , Product , Category , ProductImage_Filter

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage_Filter)


class ProductImage_Filter(admin.TabularInline):
    model = Product
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImage_Filter]