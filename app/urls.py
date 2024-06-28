from django.urls import path
from.views import*

urlpatterns =[
    path('',index, name='index'),
    path('todos/',todo_list,name='todo_list')
]