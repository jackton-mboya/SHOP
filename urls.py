from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('services/', views.services, name='services'),
    path('single/', views.single, name='single'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('help/', views.help, name='help'),
    path('terms/', views.terms, name='terms'),
    path('meetups/', views.meetups, name='meetups'),
    path('shop/', views.shop, name='shop'),
    path('help_desk/', views.help_desk, name='help_desk'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('handbook/', views.handbook, name='handbook'),
    path('find_designers/', views.find_designers, name='find_designers'),
    path('find_developers/', views.find_developers, name='find_developers'),
    path('teams/', views.teams, name='teams'),
    path('API/', views.API, name='API'),
    path('advertise/', views.advertise, name='advertise'),
    path('privacy/', views.privacy, name='privacy'),
    path('cart/', views.cart_view, name='cart'),
    path('web-design/', views.web_design, name='web_design'),
    path('ecommerce/', views.ecommerce, name='ecommerce'),
    path('branding/', views.branding, name='branding'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('payment/', views.payment_view, name='payment'),
    path('process_payment/', views.process_payment_view, name='process_payment'),
    # API routes
    path('api/subscribers/', views.SubscriberListCreateView.as_view(), name='subscriber_list_create'),
    path('api/subscribers/<int:pk>/', views.SubscriberDetailView.as_view(), name='subscriber_detail'),
    path('api/contact_messages/', views.ContactMessageListCreateView.as_view(), name='contact_message_list_create'),
    path('api/contact_messages/<int:pk>/', views.ContactMessageDetailView.as_view(), name='contact_message_detail'),
    # New subscription success URL
    path('subscription_success/', views.subscription_success, name='subscription_success'),
]




