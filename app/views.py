from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import customer,cart,Product,orderPlaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#def home(request):
# return render(request, 'app/home.html')

class productView(View):
    def get(self,request):
        mobiles=Product.objects.filter(category='M')
        cloths=Product.objects.filter(category='C')
        books=Product.objects.filter(category='B')
        return render(request,'app/home.html',{'mobiles':mobiles,'clothing':cloths,'book':books})


#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class productDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:
            item_already_in_cart=cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})


@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        Cart=cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in cart.objects.all()if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price)
                amount+=tempamount
                total_amount=amount+shipping_amount
            return render(request, 'app/addtocart.html',{'carts':Cart,'totalamount':total_amount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')



def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        #print(prod_id)
        c=cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in cart.objects.all()if p.user==request.user]
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)



def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        #print(prod_id)
        c=cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in cart.objects.all()if p.user==request.user]
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)



def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        #print(prod_id)
        c=cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in cart.objects.all()if p.user==request.user]
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount

        data={
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)


        


def buy_now(request):
 return render(request, 'app/buynow.html')

#def profile(request):
# return render(request, 'app/profile.html')

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Profile Updated Successfully!!')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})



def address(request):
    add=customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
    op=orderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})





def mobile(request,data=None):
    if data== None:
        mobiles=Product.objects.filter(category="M")
    elif data=='Redmi' or data=='Samsung' or data=='Apple' or data=='mi':
        mobiles=Product.objects.filter(category="M").filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category="M").filter(discounted_price__lt=20000)
    elif data=='above':
        mobiles=Product.objects.filter(category="M").filter(discounted_price__gt=20000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles})



#def login(request):
 #return render(request, 'app/login.html')


 

#def customerregistration(request):
# return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Sucessfully Registered!!')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})



@login_required
def checkout(request):
    user=request.user
    add=customer.objects.filter(user=user)
    cart_items=cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70
    totalamount=0.0
    cart_product=[p for p in cart.objects.all()if p.user==request.user]
    if cart_product:
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount
        totalamount=amount+shipping_amount
    return render(request, 'app/checkout.html',{'add': add,'totalamount':totalamount,'cart_items':cart_items})

@login_required
def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    Customer=customer.objects.get(id=custid)
    Cart=cart.objects.filter(user=user)
    for c in Cart:
        orderPlaced(user=user, customer=Customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
