from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    Featured_Products = Product.objects.order_by('priority')[:4] #[:4]is indicating first 4product in the priority list
    Latest_Products = Product.objects.order_by('-id')[:4] #(-id) is indicate letest id in the database
    context = {
        'Featured_Products':Featured_Products,
        'Latest_Products':Latest_Products
    }
    return render(request,'index.html',context)

def list_product(request,pk):
    """_summary_
    returns product list page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page = 1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('-priority') #order by is inticated to data sorted by the argument pat-24 14.03
    product_paginator = Paginator(product_list,4) #paginator objects passing for how may prodduct listing a single page
    product_list=product_paginator.get_page(page)  #part-23 8.54
    context={'products':product_list}
    return render(request, 'products.html',context)


def product_details(request,pk):
    prd = Product.objects.get(pk=pk)
    context={'prd':prd}
    return render(request,'product_details.html',context)