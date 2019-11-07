from rest_framework import serializers

from .models import item
class ItemSer(serializers.Serializer):
    Name = serializers.CharField(max_length=100)
    Price = serializers.IntegerField()
    Amount = serializers.IntegerField()

    def create(self, validated_data):
        return item.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Amount = validated_data.get('Amount', instance.Amount)
        instance.save()
        return instance

class ItemSerGet(serializers.Serializer):
    itemID = serializers.IntegerField()
    Name = serializers.CharField(max_length=100)
    Price = serializers.IntegerField()
    Amount = serializers.IntegerField()