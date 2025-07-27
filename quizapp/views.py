from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import BookSerializer
from .models import Book,Survey
from .model_forms import DynamicSurveyForm
from django.shortcuts import get_object_or_404

class AllBookView(APIView):
    def get(self, request):
        books=Book.objects.select_related()
        if not books:
            return Response({"data":[]},status=status.HTTP_204_NO_CONTENT)
        ser_data=BookSerializer(instance=books,many=True)
        return Response({"data": ser_data.data},status=status.HTTP_200_OK)
    
class SurveyView(APIView):
    # {
    # "survey_id":1,
    # "age":22,
    # "email":"temp@gmail.com"
    # }

    def post(self,request):
        survey_id=request.data["survey_id"]
        survey=get_object_or_404(Survey,pk=survey_id)
        form = DynamicSurveyForm(data=request.data, survey_instance=survey)
        if form.is_valid():
            return Response({
                "message": "Survey submitted successfully","data": form.cleaned_data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)

