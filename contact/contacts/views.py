from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Extract cleaned data
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Format message body
            full_message = f"From: {name} <{sender_email}>\n\n{message}"

            # Compose email with reply_to
            email = EmailMessage(
                subject=subject,
                body=full_message,
                from_email='patiencesitati99@gmail.com',  # Must match your Gmail or SMTP settings
                to=['patiencesitati99@gmail.com'],
                reply_to=[sender_email],  # This makes "reply" go to the sender
            )
            email.send()
            
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/#contact')  # Make sure this URL name maps to your contact page
        else:
            messages.error(request, "There was an error. Please correct the form below.")
    else:
        form = ContactForm()
    return render(request, 'contacts/index.html', {'form': form})


def health_check(request):
    return JsonResponse({'status': 'ok'})




