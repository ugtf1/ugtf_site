from django import forms
from .models import ScopingCall, BriefMessage, ContactMessage

class ScopingCallForm(forms.ModelForm):
    class Meta:
        model = ScopingCall
        fields = ["name", "phone", "email", "preferred_contact_method"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "preferred_contact_method": forms.Select(),
        }

class BriefMessageForm(forms.ModelForm):
    class Meta:
        model = BriefMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Your brief"}),
        }

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["email", "phone", "message", "subscribe"]
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone"}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "What are we building today?"}),
        }