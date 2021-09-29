from product.views import   CategoryDetailView, CategoryListView, ImageUploadListView,ProductDetailView, ProductListView
from django.urls import path

urlpatterns=[
    path('categories',CategoryListView.as_view(),name='category'),
    path('categories/<int:pk>',CategoryDetailView.as_view(),name='single_category'),
    path('products',ProductListView.as_view(),name='products'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='singleproduct'),
    path('upload',ImageUploadListView.as_view(),name='uplad'),
    #  path('orderItem',orderItemView.as_view(),name='orderItem'),
    # path('convert',MyTextView.as_view(),name="converts")
]