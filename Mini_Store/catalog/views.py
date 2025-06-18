from django.shortcuts import render
from  users.models import Category , Product , ProductImage_Filter
from . import functions
# Create your views here.
get_page = ""
def catalog_product(request):
    return render(request,"catalog/catalog.html")


def product_list(request):
    get_page = request.GET.get("step")
    category = Category.objects.get(name=get_page)
    list_products = category.product_set.all();
    all_cat_name = functions.category_name_or_slug("name")
    if request.method == "POST":
        search = request.POST.get("q")
        list_products = functions.product_search(search)
        get_page = search
    context = {
        "page":get_page,
        "products":list_products,
        "categories":all_cat_name
    }
    return render(request,"catalog/catalog_product.html",context=context)
