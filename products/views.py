from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/new_product.html', {'products': products})
    
    def post(self, request):
        product_id = request.POST.get('id')
        cart_value = [request.session.get('cart', 0)]
        cart_value.append(product_id)
        request.session['cart'] = cart_value
        return redirect('product')

