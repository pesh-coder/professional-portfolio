from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-input bg-gray-800 text-white px-4 py-3 rounded w-full focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-input bg-gray-800 text-white px-4 py-3 rounded w-full focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
                'class': 'form-input bg-gray-800 text-white px-4 py-3 rounded w-full focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'class': 'form-input bg-gray-800 text-white px-4 py-3 rounded w-full focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
        }

