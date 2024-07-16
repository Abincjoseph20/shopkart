from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'index.html')

def list_product(request):
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
    product_list=Product.objects.all()
    product_paginator = Paginator(product_list,4) #paginator objects passing for how may prodduct listing a single page
    product_list=product_paginator.get_page(page)  #part-23 8.54
    context={'products':product_list}
    return render(request, 'products.html',context)


def product_details(request):
    # prd = Product.objects.get(pk=pk)
    return render(request,'product_details.html')