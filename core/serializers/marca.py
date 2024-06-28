from rest_framework.serializers import ModelSerializer

from core.serializers import marca


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = marca
        fields = "__str__"
