from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from wiki.models import Page
from api.serializers import PageSerializer
# from api.serializers import ChoiceSerializer

class PageList(APIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(APIView):
    def get(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        data = PageSerializer(page).data
        return Response(data)
