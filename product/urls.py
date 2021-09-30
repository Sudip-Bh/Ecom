from product.views import  CartAddView, CartListView, CartUpdateView, CategoryDetailView, CategoryListView, ImageUploadListView, ImageUploadView, OrderItemView, OrderView,  ProductDetailView, ProductListView
from django.urls import path

urlpatterns=[
    path('categories',CategoryListView.as_view(),name='category'),
    path('categories/<int:pk>',CategoryDetailView.as_view(),name='singlecategory'),

    path('products',ProductListView.as_view(),name='products'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='singleproduct'),

    path('upload',ImageUploadListView.as_view(),name='upload'),

    path('orderitem/',OrderItemView.as_view(),name='orderitem'),
    path('cartadd',CartAddView.as_view(),name='cartadd'),
    path('cartlist',CartListView.as_view(),name='cartlist'),
    path('cartup/<int:pk>',CartUpdateView.as_view(),name='cartupdate'),
    # path('cartdel/<int:pk>',CartDeleteView,name='cartdelete'),

    path('order',OrderView.as_view(),name='order'),
]