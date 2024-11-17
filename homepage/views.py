
# Create your views here.
# homepage/views.py
from django.http import HttpResponse
from .models import Watch, Wishlist, Cart
from django.contrib.auth.decorators import login_required

def home(request):
    watches=Watch.objects.all()
    context={'watches':watches}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

from django.shortcuts import render, redirect, get_object_or_404
from .forms import WatchUploadForm
from django.contrib import messages

def upload_watch(request):
    if request.method == 'POST':
        form = WatchUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the watch details and image to the database
            messages.success(request, "Watch uploaded successfully!")
            return redirect('home')  # Redirect to the homepage after a successful upload
        else:
            messages.error(request, "Error uploading the watch. Please check the form and try again.")
    else:
        form = WatchUploadForm()  # Display an empty form for GET requests
    
    return render(request, 'upload.html', {'form': form}) 

#watch list page
def watch_list(request):
    watches = Watch.objects.all()
    return render(request, 'watch_list.html', {'watches': watches})

@login_required
def add_to_wishlist(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.watches.add(watch)
    return redirect('home')

@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_cart(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.watches.add(watch)
    return redirect('home')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def remove_from_wishlist(request, watch_id):
    if request.method == "POST":  # Ensure it's a POST request
        watch = get_object_or_404(Watch, id=watch_id)
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist.watches.remove(watch)  # Remove the watch from the wishlist
        return redirect('view_wishlist')  # Ensure this matches the URL name for your wishlist page
    return redirect('view_wishlist')

@login_required
def remove_from_cart(request, watch_id):
    if request.method == "POST":  # Ensure it's a POST request
        watch = get_object_or_404(Watch, id=watch_id)
        cart = get_object_or_404(Cart, user=request.user)
        cart.watches.remove(watch)  # Remove the watch from the cart
        return redirect('view_cart')  # Ensure this matches the URL name for your cart page
    return redirect('view_cart')