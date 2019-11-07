from rest_framework import serializers

class ItemSer(serializers.Serializer):
    itemID = serializers.IntegerField()
    Name = serializers.CharField(max_length=100)
    Price = serializers.IntegerField()
    Amount = serializers.IntegerField()

