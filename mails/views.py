from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views.generic import FormView

from mails.forms import EmailForm


# Create your views here.
class MailListView(FormView):
    template_name = 'mails/mail.html'
    form_class = EmailForm
    success_url = '../mail'

    def form_valid(self, form):
        data = form.cleaned_data
        subject = data['subject']
        message = data['message']
        email = data['email']
        email_name = data['email_name']
        destination = data['destination']

        e_mail = EmailMessage(subject, message, email, to=[destination], reply_to=[email])
        e_mail.send()
        return super(MailListView, self).form_valid(form)
