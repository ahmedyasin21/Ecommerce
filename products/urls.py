from django.conf.urls import url
from django.urls import path
from . import views



app_name = 'products'

urlpatterns = [
  path('create',views.ProductCreateView.as_view(),name = 'product'),
  path('list',views.ProductListView.as_view(),name = 'product_list'),
  path('detail/<str:slug>',views.ProductDetailView.as_view(),name = 'product_detail'),
  path('update/<str:slug>',views.ProductUpdateView.as_view(),name ='product_update'),
  path('delete/<str:slug>',views.ProductDeleteView.as_view(),name ='product_delete'),


  #add to cart
  path('add-to-cart/<slug>/', views.add_to_cart, name='add_to_cart'),
  path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
  path('remove_single_item_from_cart/<slug>/', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),
  

]