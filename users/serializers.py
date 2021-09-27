from rest_framework import serializers
from users.models import Users, Loan

class UsersSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Users
        fields = (
            'id',
            'user_id',
            'user_type',
            'full_name',
            'phone_no',
            'password',
            'profession',
            'current_address',
            'permanent_address',
            'nid_no',
            'deposit_amount',
            'tenure',
            'opening_date',
            'photoFileName'

        )

class LoanSerializers(serializers.ModelSerializer):
    class Meta :
        model = Loan
        fields = (
            'id',
            'user_id',
            'full_name',
            'phone_no',
            'total_balance',
            'is_loan',
            'loan_amount',
            'tenure',
            'interest_rate'
        )