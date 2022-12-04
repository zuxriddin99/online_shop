from django import forms

from apps.users.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('user', 'city', 'address', 'country', 'default')
