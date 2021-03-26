from rest_framework import serializers
from .models import PrintJob
from .models import Printer

class PrintJobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PrintJob
        fields = "__all__"
    
# class PrinterSerializer(seralizers.ModelSerializer):

