from django.shortcuts import render,redirect
from .models import Customer,Orders,Products
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout   #to verify uname & pwd
from django.contrib import messages     #flash msgs if login detail false
from django.contrib.auth.decorators import login_required #if we try to open homepage directly
                                                            #then it should ask to login
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group    #for groups coz here we've admin and cust grp


'''
def register_page(request):
    #form = UserCreationForm()   #-->giving only 3 fields
    form = CreateUserForm
    context = {'form':form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('login')

    return render(request,'accounts/register.html',context)
'''

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    context = {'form':form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            group = Group.objects.get(name = 'customer')    #username will add in Group
            user.groups.add(group)
        return redirect('login')

    return render(request,'accounts/register.html',context)



@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    customers = Customer.objects.all()
    products = Products.objects.all()
    orders = Orders.objects.all()

    total_orders = len(orders)
    pending_orders = orders.filter(status ='Pending').count()
    delivered_orders = orders.filter(status ='Delivered').count()
    outfordelivery_orders = orders.filter(status ='OutforDelivery').count()

    context = {
        'customers': customers,
        'products': products,
        'orders': orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'outfordelivery_orders': outfordelivery_orders
    }

    return render(request, 'accounts/dashboard.html',context)

def userpage(request):
    return render(request,'accounts/user.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def orders(request):
    orders = Orders.objects.all()
    context = {'orders':orders}
    return render(request,'accounts/orders.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'accounts/products.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.orders_set.all()

    total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    outfordelivery_orders = orders.filter(status='OutforDelivery').count()

    context = {
        'customer': customer,
        'orders' : orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'outfordelivery_orders': outfordelivery_orders
    }

    return render(request, 'accounts/customer.html',context)