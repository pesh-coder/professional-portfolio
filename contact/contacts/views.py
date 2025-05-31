from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['patiencesitati99@gmail.com'],
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/#contact')  # Make sure this URL name maps to your contact page
        else:
            messages.error(request, "There was an error. Please correct the form below.")
    else:
        form = ContactForm()
    return render(request, 'contacts/portfolio.html', {'form': form})



