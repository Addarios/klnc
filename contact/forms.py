from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Imię i nazwisko", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jan Kowalski'}))
    email = forms.EmailField(label="Adres e-mail", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    message = forms.CharField(label="Twoja wiadomość", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))