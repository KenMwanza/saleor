from __future__ import unicode_literals
from django import forms

from payments.forms import PaymentForm

class LipaNaMpesaForm(PaymentForm):
    RESPONSE_CHOICES = (
        ('failure', 'Gateway connection error'),
	('payment-error', 'Gateway returned unsupported response'),
    )
    status = forms.ChoiceField(choices=PaymentStatus.CHOICES)
    
    

    def clean(self):
        cleaned_data = super(LipaNaMpesaForm, self).clean()
	return cleaned_data
