from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import item
from .serialaizers import ItemSer

class ItemView(APIView):
    def get(self,request):
        items = item.objects.all()
        serializer = ItemSer(items, many=True)
        return Response({"items": serializer.data})