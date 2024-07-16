from django.forms import ModelForm
from .models import *

class RecordForm(ModelForm):
    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data == '0':
            data = '1'
        return data

    class Meta:
        model = Record
        fields = ["name", "amount", "unit"]
        labels = {
            'name': 'Наименование',
            'amount': 'Количество',
            'unit': 'Ед.изм.',
            }
