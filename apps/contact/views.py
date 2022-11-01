from django.shortcuts import render, redirect
from .forms import ContactForm, Contact


# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact:contact')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
