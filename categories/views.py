from django.shortcuts import render
from shops.models import ShopProfile
# Create your views here.
from .models import ShopCategory
from django.views.generic import ListView,DetailView


class ShopCategoriesListView(ListView):
    model = ShopCategory
    template_name = "categories/categories_list.html"

    def get_queryset(self):
        return ShopCategory.objects.all()

class ShopCategoriesDetailPostView(DetailView):
    model = ShopCategory
    template_name = "categories/categories_detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoplist"] = ShopProfile.objects.filter(shop_category=self.object)[:15]
        return context

# class TagDetailBlogView(DetailView):
#     model = Tag
#     template_name = "tags/tag_detail_blog.html"


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["header_bloglist"] = Blog.objects.filter(tag__title=self.object.title)[:6]
#         return context