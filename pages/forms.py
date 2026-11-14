from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length = 50, 
        widget = forms.TextInput(attrs={'placeholder': 'Your name'})
        )
    email = forms.EmailField(

        widget = forms.EmailInput(attrs = {'placeholder': 'Your email address'})
    )
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {'placeholder': 'your message'})
        )