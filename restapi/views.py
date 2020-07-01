from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import BankBranch
from .serializers import BankBranchSerializer
from rest_framework import permissions


class ListBankDetailsView(generics.ListAPIView):
    """
    All the bank name, ifsc, address, city, district, state
    GET bank/
    GET bank/?name=<name>&city=<city>/
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        qs = BankBranch.objects.all()
        if name != None and city != None:
            qs = qs.filter(bank_name=name).filter(city=city)

        return qs


class BankDetailsIfcsView(generics.RetrieveAPIView):
    """
    Bank details, for given ifsc
    GET bank/<ifsc>/
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BankBranch.objects.filter(ifsc=self.kwargs.get('pk'))
