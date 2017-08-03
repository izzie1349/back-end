from django.core import validators
from AppTwo.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # tells form to grab all fields in User model
        fields = "__all__"

        # # tells form to exclude provided fields
        # exclude = ["field1", "field2"]
        #
        # # tells form to include provided fields
        # fields = ("field1", "field2")
