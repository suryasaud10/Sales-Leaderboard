from django import forms
from .models import SalesRecord

class SaleForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = ["agent_name", "sales_amount", "deals_count"]

    def clean_sales_amount(self):
        value = self.cleaned_data["sales_amount"]
        if value < 0:
            raise forms.ValidationError("Sales amount cannot be negative")
        return value

    def clean_deals_count(self):
        value = self.cleaned_data["deals_count"]
        if value < 0:
            raise forms.ValidationError("Deals count cannot be negative")
        return value
