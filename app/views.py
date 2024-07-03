from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from.models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def index(request):
    person1 = {
        "name": "Fatema",
        "age": 21,
        "is_married": True
    }
    person2 ={
        "name": "Royel",
        "age": 18,
        "is_married":False
    }
    person_list =[person1,person2]
    return Response(person_list)

@api_view(['Get'])
def todo_list(request):
    todos = Todo.objects.all()

    serializer = TodoListSerializer(todos, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    serializer = TodoDetailSerializer(todo)
    return Response(serializer.data)