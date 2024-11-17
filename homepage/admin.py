from django.contrib import admin

# Register your models here.
from .models import Watch
class WatchUploadAdmin(admin.ModelAdmin):
    list_display =('name', 'description', 'price', 'image') 
    list_filter = ('name', 'price')
    search_fields = ('description', 'price')
    fields = ['name', 'description', 'price', 'image']

admin.site.register(Watch,WatchUploadAdmin)

from .models import Wishlist, Cart
admin.site.register(Wishlist)
admin.site.register(Cart)
