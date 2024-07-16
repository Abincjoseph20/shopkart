from django.shortcuts import render
from .models import Product
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
    return render(request, 'products.html')

def product_details(request):
    # prd = Product.objects.get(pk=pk)
    return render(request,'product_details.html')