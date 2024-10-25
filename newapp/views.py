from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializer import TaskSerializer

@api_view(['GET'])
def get_tasks(request: Request) -> Response:
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_task(request: Request, id: int) -> Response:
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task)

    return Response(serializer.data)

@api_view(['POST'])
def store_task(request: Request) -> Response:
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['PATCH'])
def update_task(request: Request, id: int) -> Response:
    task = get_object_or_404(Task, id=id)
    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_task(request: Request, id: int) -> Response:
    task = get_object_or_404(Task, id=id)
    
    task.delete()

    return Response("Task deleted successfully")