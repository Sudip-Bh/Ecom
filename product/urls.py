from product.views import BookDetailView, BookListView, CategoryDetailView, CategoryListView, ImageUploadListView, ImageUploadView,  ProductDetailView, ProductListView
from django.urls import path

urlpatterns=[
    path('categories',CategoryListView.as_view(),name='category'),
    path('categories/<int:pk>',CategoryDetailView.as_view(),name='single_category'),
    path('books',BookListView.as_view(),name='books'),
    path('books/<int:pk>',BookDetailView.as_view(),name="singlebook"),
    path('products',ProductListView.as_view(),name='products'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='singleproduct'),
    path('upload',ImageUploadView.as_view(),name='uploadimg'),
    path('upload1',ImageUploadListView.as_view(),name='uplad'),
    # path('convert',MyTextView.as_view(),name="converts")
]