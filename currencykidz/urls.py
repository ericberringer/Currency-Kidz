from currencykidzapi.views.currency import CurrencyView
from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from currencykidzapi.views import register_user, login_user
from currencykidzapi.views import CurrencyView, DepositEventView, WithdrawalEventView, ProfileView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'currency', CurrencyView, 'currency')
router.register(r'deposit_event', DepositEventView, 'deposit_events')
router.register(r'withdrawal_event', WithdrawalEventView, 'withdrawal_events')
router.register(r'profile', ProfileView, 'profile')


urlpatterns = [
    path('admin/', admin.site.urls),
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]