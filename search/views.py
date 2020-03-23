from django.shortcuts import render,redirect
from django.db.models import Q
from products.models import Product
from .amazon import ReadAsinAmzn
from .flipkart import ReadAsinflip
from .snapdeal import ReadAsinSnap


def clean(query):
    flipkart_data = ReadAsinflip(query)
    # Amazon_data = ReadAsinAmzn(query)
    Amazon_data = []
    Snapdeal_data = ReadAsinSnap(query)
    data = [flipkart_data,Snapdeal_data,Amazon_data]
    return data


def do_search(request):
    print(request.POST)
    query = request.POST['q']

    form = clean(query)
    Flipkart_product = form[0]
    for item_details in Flipkart_product:
        product_details_Fkrt = Product.objects.create(brand=item_details[0],name=item_details[1]+'|'+query.capitalize(),price=item_details[2],rating=item_details[3],
                                                      image=item_details[4],url=item_details[5],seller="Flipkart")
    Snapdeal_product = form[1]
    for item_details in Snapdeal_product:
        product_details_Snap = Product.objects.create(brand=item_details[0],name=item_details[1]+'|'+query.capitalize(),price=item_details[2],rating=item_details[3],
                                                      image=item_details[4],url=item_details[5],seller="Snapdeal")
    Amazon_product = form[2]
    for item_details in Amazon_product:
        product_details_Amzn = Product.objects.create(brand=item_details[0],name=item_details[1],price=item_details[2],rating=item_details[3],
                                                          image=item_details[4],url=item_details[5],seller="Amazon")
    products = Product.objects.filter(name__icontains=query).distinct()
    context = {
        "products": products,
    }
    return render(request,"search/result.html",context)


