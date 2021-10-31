from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'categories'

urlpatterns = [
    path('home/',views.ShopCategoriesListView.as_view(),name='all_categories'),
    path('<str:slug>/detail/shops/',views.ShopCategoriesDetailPostView.as_view(),name='categories_detail'),
    # path('<int:pk>/<str:slug>/detail/blog/',views.TagDetailBlogView.as_view(),name='tag_detail_blog'),
]