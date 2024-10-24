from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_tasks(request: Request) -> Response:
    pass

@api_view(['GET'])
def get_task(request: Request) -> Response:
    pass

@api_view(['POST'])
def store_task(request: Request) -> Response:
    pass

@api_view(['PATCH'])
def update_task(request: Request) -> Response:
    pass

@api_view(['DELETE'])
def delete_task(request: Request) -> Response:
    pass

