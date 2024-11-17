from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Watch(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='watch_images/')

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watches = models.ManyToManyField('Watch', related_name='wishlists')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watches = models.ManyToManyField('Watch', related_name='carts')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"