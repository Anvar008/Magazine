from django import forms
from magazine.models import SendEmail


class EmailForm(forms.ModelForm):
    class Meta:
        model = SendEmail
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 600px; border'}),
        }
