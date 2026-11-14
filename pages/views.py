from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    # POST : the visitor has submitted the form
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():# django valites all fields and returns a dictionary with the cleaned data
             #Extract the cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #Build the email message
            message_body = (
                f" You have a new message from your portfolio contact form.\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message:\n{message}"
            )
            # try to send the email
            try:
                send_mail(
                    "Message from your portfolio contact form", # subject line
                    message_body, # message body
                    email, # From: visitor's email address
                    ["jparra.sdgku@gmail.com"], # To: your email address
                )
                #Success: Reset the form and show a confirmation message
                form = ContactForm() # Reset the form
                return render(request, "pages/contact.html", {"form": form})
            except Exception:
                #Send email failed: pass error message to the template
                return render(request, "pages/contact.html", {"form": form})
        else: 
            # form is not valid: pass the form with errors to the template
            return render(request, "pages/contact.html", {"form": form})
    else: # GET: the visitor is accessing the contact page for the first time-- show an empty form
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})