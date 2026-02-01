from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('images', ProductImageViewSet)
router.register('orders', OrderViewSet, basename='order')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),

    path(
        'categories/<int:category_id>/products/',
        CategoryProductsViewSet.as_view({'get': 'list'})
    ),
    path(
        'products/<int:product_id>/images/',
        ProductImagesViewSet.as_view({'get': 'list'})
    ),
    path(
        'products/<int:product_id>/comments/',
        ProductCommentsViewSet.as_view({'get': 'list'})
    ),
]
