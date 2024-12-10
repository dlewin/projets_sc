from rest_framework import serializers
from .models import Yuze

class YuzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuze
        fields = '__all__'

