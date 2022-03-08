from pyexpat import model
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']
class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ['id','user_id','usage_type_id','usage_at','date_created','amount']

        