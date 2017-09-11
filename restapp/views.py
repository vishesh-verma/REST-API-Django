# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializers import stockSerializer

class stockList(APIView):

    def get(self,request):
        stocks=stock.objects.all()
        serializer = stockSerializer(stocks, many=True)
        return Response(serializer.data)
