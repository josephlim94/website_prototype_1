from django import forms
from .models import GeneralTable

class GeneralTableForm(forms.ModelForm):
    class Meta:
        model = GeneralTable
        fields = "__all__"