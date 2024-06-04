from django.shortcuts import render
from products.models import Product


# Create your views here.

def search(request):
    item_name = request.GET.get('item_name')
    query = Product.objects.filter(name__icontains=item_name)

    return render(request, 'search.html', {'query': query, 'item_name': item_name})
