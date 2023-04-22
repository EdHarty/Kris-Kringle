from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import NewsLetter
from .forms import ContactForm, NewsletterForm


def contact(request):
    """ To handle the customer contact form """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. Processing\
                query.')
            return redirect(reverse('contact'))

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def newsletter(request):
    """ To handle newsletter subscription """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetter.objects.filter(
                    email=instance.email).exists():
                messages.error(request, 'Subscription already exists')
            else:
                instance.save()
                messages.success(request, 'Thank you for signing up to our \
                    newsletter!')
                return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'newsletter.html', context)


def unsubscribe(request):
    """ To handle newsletter unsubscriptions """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetter.objects.filter(
                    email=instance.email).exists():
                NewsLetter.objects.filter(
                    email=instance.email).delete()
                messages.success(request, 'You have unsubscribed from our\
                newsletter')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'The email entered is not valid.\
                    Please re-enter email.')

    context = {
        'form': form,
    }

    return render(request, 'Unsubscribe.html', context)
