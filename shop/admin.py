from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductImage,
    Comment,
    Order,
    ProductLike
)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [ProductImageInline]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    search_fields = ('user__username', 'product__name')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status')
    list_filter = ('status',)



@admin.register(ProductLike)
class ProductLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    search_fields = ('user__username', 'product__name')
