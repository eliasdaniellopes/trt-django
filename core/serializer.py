from rest_framework import serializers

from .models import Registros_filtrados
class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registros_filtrados
        fields = ('id', 'titulo', 'linkMag')