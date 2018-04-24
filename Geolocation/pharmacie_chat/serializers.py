from rest_framework import serializers
from pharmacie_chat.models import donnee_pharmacie, LANGUAGE_CHOICES

class DonneepharmacieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.URLField(max_length=100, required=False, default='nothing')
    url_map = serializers.CharField(max_length=100, required=True)
    telephone = serializers.CharField()
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    #language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `pharmacie_chat` instance, given the validated data.
        """
        return pharmacie_chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.nom = validated_data.get('nom', instance.nom)
        instance.url_map = validated_data.get('url_map', instance.url_map)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.language = validated_data.get('language', instance.language)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance
   
class ProximiteSerializer(serializers.Serializer):
      distance = serializers.CharField(required=False)
