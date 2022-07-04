from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


def index(request):
    return HttpResponse("TESTING API, SUCCESS!!")


class DataUploaderView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    # TODO implement the multi file S3 uploader
