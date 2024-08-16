from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Subscriber, ContactMessage
from .forms import SubscriptionForm, ContactForm
from .serializers import SubscriberSerializer, ContactMessageSerializer
from django.core.mail import send_mail


# Existing views
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Subscriber.objects.create(email=email)
            send_mail(
                'Subscription Confirmation',
                'Thank you for subscribing!',
                'jacktonmboya1@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('subscription_success')  # Redirect to a thank-you page
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})



def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    contact_info = {
        'contact_address': '423 Utawala, Nairobi, Kenya',
        'contact_phone': '+254799877727',
        'contact_email': 'jacktonmboya1@gmail.com',
        'contact_url': 'http://jacktonmboya.com'
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Contact Message Received',
                'Thank you for reaching out! We will get back to you soon.',
                'jacktonmboya1@gmail.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {
        'form': form,
        **contact_info
    }

    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')


def services(request):
    return render(request, 'services.html')


def single(request):
    return render(request, 'single.html')


def help(request):
    return render(request, 'help.html')


def terms(request):
    return render(request, 'terms.html')


def meetups(request):
    return render(request, 'meetups.html')


def help_desk(request):
    return render(request, 'help_desk.html')


def shop(request):
    return render(request, 'shop.html')


def privacy(request):
    return render(request, 'privacy.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def handbook(request):
    return render(request, 'handbook.html')


def find_developers(request):
    return render(request, 'find_developers.html')


def find_designers(request):
    return render(request, 'find_designers.html')


def teams(request):
    return render(request, 'teams.html')


def advertise(request):
    return render(request, 'advertise.html')


def API(request):
    return render(request, 'API.html')


def cart_view(request):
    return render(request, 'cart.html')


def contact_success(request):
    return render(request, 'contact_success.html')


def web_design(request):
    return render(request, 'web_design.html')


def ecommerce(request):
    return render(request, 'ecommerce.html')


def branding(request):
    return render(request, 'branding.html')


def payment_view(request):
    return render(request, 'payment.html')


def subscription_success(request):
    return render(request, 'subscription_success.html')


def process_payment_view(request):
    if request.method == 'POST':
        return redirect('payment')
    return render(request, 'payment.html')

# API views
class SubscriberListCreateView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class SubscriberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class ContactMessageListCreateView(generics.ListCreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class ContactMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
