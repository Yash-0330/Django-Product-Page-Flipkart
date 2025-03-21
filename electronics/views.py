from django.shortcuts import render,redirect, get_object_or_404
from .models import product
from .forms import productForm
# Create your views here.

def home(request):
    return render(request,'electronics/home.html')

def product_detail(request):
    prod=product.objects.all()
    form = productForm()
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            form = productForm()
    return render(request,'electronics/product_detail.html',{"prod":prod,"form":form})
def delete_product(request,id):
    prod = get_object_or_404(product,id=id)
    prod.delete()
    return redirect("product_detail")


def update_product(request,id):
    prod = get_object_or_404(product,id=id)
    form = productForm(instance=prod)       
    
    if request.method == 'POST':
        form = productForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('product_detail')
    else:
        form = productForm(instance=prod)
        return render(request,'electronics/update_product.html',{"form":form})





