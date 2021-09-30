from product.views import  CartAddView, CartDeleteView, CartListView, CartUpdateView, CategoryDetailView, CategoryListView, ImageUploadListView, ImageUploadView, OrderItemView, OrderView,  ProductDetailView, ProductListView
from django.urls import path

urlpatterns=[
    path('categories',CategoryListView.as_view(),name='category'),
    path('categories/<int:pk>',CategoryDetailView.as_view(),name='single_category'),
    path('products',ProductListView.as_view(),name='products'),
    # path('product/<int:pk>',ProductDetailView.as_view(),name='singleproduct'),
    path('upload',ImageUploadListView.as_view(),name='upload'),
    path('orderitem/',OrderItemView.as_view(),name='orderitem'),
    path('cartitem',CartAddView.as_view(),name='caritem'),
    path('cartlist',CartListView.as_view(),name='cartlist'),
    path('cartup/<int:pk>',CartUpdateView.as_view(),name='cartup'),
    path('cartdel/<int:pk>',CartDeleteView,name='cartdel'),
    path('products/<slug>/',ProductDetailView.as_view(),name='prodcuts'),
    path('order',OrderView.as_view(),name='order'),
    # path('convert',MyTextView.as_view(),name="converts")
]