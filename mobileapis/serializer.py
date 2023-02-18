from django.contrib.auth.models import User
from rest_framework import serializers
from mobileapis.models import *


# ForMobile serializer
class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit

        fields = "__all__"

