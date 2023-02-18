from .models import Clent
from rest_framework import serializers


class ClentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clent
        fields = ['id','username', 'clent_phone_number', 'kafil' , 'kafil_phone_number']
