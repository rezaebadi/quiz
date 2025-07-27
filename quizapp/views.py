from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import BookSerializer
from .models import Book

class AllBookView(APIView):
    def get(self, request):
        books=Book.objects.select_related()
        if not books:
            return Response({"data":[]},status=status.HTTP_204_NO_CONTENT)
        ser_data=BookSerializer(instance=books,many=True)
        return Response({"data": ser_data.data},status=status.HTTP_200_OK)
