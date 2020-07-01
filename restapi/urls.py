# start
from django.urls import path, re_path
from .views import ListBankDetailsView, BankDetailsIfcsView

urlpatterns = [
    re_path(r'^bank/$', ListBankDetailsView.as_view(), name="banks-all"),
    re_path(r'^bank$', ListBankDetailsView.as_view(), name="banks-all"),
    path('bank/<str:pk>/', BankDetailsIfcsView.as_view(), name="bank-details")
]
