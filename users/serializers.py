from rest_framework import serializers
from users.models import Users

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