from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    
    class Meta:
        model=Page
        fields=['title', 'content', 'order']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}), #el atributo placeholder pone un texto asi como suave dentro del cuadro
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'order':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}), 
        }

        labels={'title':'', 'order':'', 'content':''} #Esto es para quitar los titulos, pura  estetica