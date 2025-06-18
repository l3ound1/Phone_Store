from users.models import Product , Category

def category_name_or_slug(str):
    all_category = Category.objects.all()
    all_category_name_or_slug = []
    if str == "name":
        for i in all_category:
            all_category_name_or_slug.append(i.name)
        return all_category_name_or_slug
    else:
        for i in all_category:
            all_category_name_or_slug.append(i.slug)
        return all_category_name_or_slug
    
def product_search(search_request):
    if search_request.isdigit():
        return []

    products = Product.objects.filter(name__icontains=search_request)
    filtered = [
        p for p in products 
        if not p.name.lower().startswith(search_request.lower()) 
        and not p.name.lower().endswith(search_request.lower())
    ]

    if not filtered:
        search_request = search_request.replace(" ", "")
        tags = Product.objects.values_list("tag", flat=True)
        for tag in tags:
            for word in tag.split():
                if word.lower() in search_request.lower():
                    return Product.objects.filter(tag__icontains=word)
                    
    return  Product.objects.filter(name__icontains=search_request)

