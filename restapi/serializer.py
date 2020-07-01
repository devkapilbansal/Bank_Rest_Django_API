#start
from rest_framework import serializers
from .models import BankBranch


class BankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankBranch
        fields = ["ifsc", "bank_name", "branch", "address", "city", "district", "state"]
