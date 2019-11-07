from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import item
from .serialaizers import ItemSer, ItemSerGet


class ItemView(APIView):
    def get(self, request):
        items = item.objects.all()
        serializer = ItemSerGet(items, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        item = request.data.get('item')
        serializer = ItemSer(data=item)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "Item '{}' created".format(item_saved.Name)})

class OneItemView(RetrieveUpdateDestroyAPIView):
    queryset = item.objects.all()
    serializer_class = ItemSerGet