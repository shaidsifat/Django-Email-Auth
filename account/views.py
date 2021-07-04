from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from  account.serializers import SnippetSerializer
# Create your views here.

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Name = form.cleaned_data.get('Name')
            Password = form.cleaned_data.get('Password')
            user = authenticate(username=Name, password=Password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def home1(request):
    list = User.objects.all()
    context ={
        'collages':list
    }
    return render(request,'home.html',context)

@api_view(['GET','POST'])
def product(request):
   if request.method == 'GET':
   	  list = User.objects.all()
   	  serializer =  SnippetSerializer(list,many=True)
   	  return Response(serializer.data)


   elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
        	 serializer.save()
        	 return Response(serializer.data,status=status.TTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	



@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        list = User.objects.get(id=pk)

    except Product.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = SnippetSerializer(list)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)