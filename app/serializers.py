from rest_framework import serializers
from.models import *

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        #komgulo dkhaty holy fields er pori borty exclude bebohar korty hoby
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        depth = 1