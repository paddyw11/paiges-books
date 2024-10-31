from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
"""
views.py for contact app

"""


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            message_body = f"Message from {name} ({email}):\n\n{message}"

            try:
                send_mail(
                    subject,
                    message_body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['paigesbookshop@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for contacting us. \
                    We will get back to you shortly.')
                return redirect('contact_us')
            except Exception as e:
                messages.error(request, 'There was an error sending your \
                    message. Please try again later.')
                print(f"Error sending email: {e}")
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})


def contact_us(request):
    return render(request, 'contact/contact_us.html')
