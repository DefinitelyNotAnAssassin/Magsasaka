from TransactionRecord.models import TransactionRecord
from django.forms import ModelForm
import django.forms as forms 


class TransactionRecordForm(ModelForm): 
    
    class Meta: 
        model = TransactionRecord
        fields = '__all__'
        widgets = {
            'beneficiary': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline', 'placeholder': 'Enter BH ID Number'}),
            'date': forms.DateInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline', 'placeholder' : 'MM/DD/YY', 'type': 'date'}),
            'service': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'remarks': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
        }