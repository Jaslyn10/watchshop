from django import forms
from .models import Watch 

class WatchUploadForm(forms.ModelForm):
    
    # Custom form field attributes for better control over the form display
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),required=True)

    class Meta:
        model = Watch  # Link to the Watch model
        fields = ['name', 'description', 'price', 'image']  
