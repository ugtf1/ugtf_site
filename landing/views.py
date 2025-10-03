from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ScopingCallForm, BriefMessageForm, ContactMessageForm
from .models import MailingListSubscriber

# Create your views here.
def index(request):
    scoping_form = ScopingCallForm()
    brief_form = BriefMessageForm()
    contact_form = ContactMessageForm()
    return render(
        request,
        "landing/index.html",
        {
            "scoping_form": scoping_form,
            "brief_form": brief_form,
            "contact_form": contact_form,
        },
    )

def submit_scoping_call(request):
    if request.method == "POST":
        form = ScopingCallForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your scoping call request has been received.")
        else:
            messages.error(request, "Please review your responses.")
    return redirect("home")

def submit_brief(request):
    if request.method == "POST":
        form = BriefMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message received. We'll get back to you shortly.")
        else:
            messages.error(request, "Please review your responses.")
    return redirect("home")

def submit_contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            obj = form.save()
            if obj.subscribe:
                MailingListSubscriber.objects.get_or_create(email=obj.email)
            messages.success(request, "Thanks for contacting UGTF. We’ll reach out soon.")
        else:
            messages.error(request, "Please review your responses.")
    return redirect("home")

def about(request):
    return render(request, "landing/about.html")

def services(request):
    return render(request, "landing/services.html")