from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
