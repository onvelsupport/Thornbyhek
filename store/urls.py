from django.urls import path
from . import views

urlpatterns = [
    # Main Pages
    path('', views.home, name='home'),
    path('collection/', views.collection, name='collection'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Cart
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<str:cart_key>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<str:cart_key>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),

    # Checkout
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),

    # Information Pages
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('refund/', views.refund, name='refund'),
    path('privacy/', views.privacy, name='privacy'),
    path('faq/', views.faq, name='faq'),
    path('tracking/', views.tracking, name='tracking'),


    path('search/', views.search, name='search'),
    path('favourites/', views.favourites, name='favourites'),
    path('favourite/toggle/<int:product_id>/', views.toggle_favourite, name='toggle_favourite'),

# Payment
path('checkout/payment/<int:order_id>/', views.choose_payment_method, name='choose_payment_method'),

path('checkout/stripe-a/<int:order_id>/', views.stripe_checkout_a, name='stripe_checkout_a'),

path('checkout/stripe-b/<int:order_id>/', views.stripe_checkout_b, name='stripe_checkout_b'),

path('checkout/square/<int:order_id>/', views.square_checkout, name='square_checkout'),

# Stripe Webhooks
path(
    'stripe/test/webhook/',
    views.stripe_test_webhook,
    name='stripe_test_webhook'
),

path(
    'stripe/live/webhook/',
    views.stripe_live_webhook,
    name='stripe_live_webhook'
),

# Square Webhook
path(
    'square/webhook/',
    views.square_webhook,
    name='square_webhook'
),


    path('tracking/result/', views.tracking_result, name='tracking_result'),

    #path('test-order-email/', views.test_order_email, name='test_order_email'),
]