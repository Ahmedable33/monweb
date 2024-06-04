from django import forms

from mails.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ['date_sent']

    def clean(self):
        cleaned_data = super()

