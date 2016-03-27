from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = "Sign Up Now"
    #if request.user.is_authenticated():
    #    title = "Welcome %s" %(request.user)

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        #     instance.full_name = "James"
        instance.save()
        context = {
            "title": "Thank you"
        }


    return render(request, "home.html", context)

def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)

    context = {
        "form": form,
        "title": title,
    }

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
    # if form.is_valid():
    #     for key, value in form.cleaned_data.iteritems():
    #         print key, value
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s" %(
                form_full_name,
                form_message,
                form_email)

        send_mail(subject, contact_message, from_email,
                to_email, fail_silently=False)
        return HttpResponseRedirect('/thanks/')

    return render(request, "forms.html", context)
