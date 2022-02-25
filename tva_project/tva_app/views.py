from encodings import search_function
from unicodedata import name
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .pagination import MyPagination1,MyPagination2
from .models import tva_table
from .serializers import usersSerializer


# For Get Request ====> localhost/users

class ListApiView(generics.ListAPIView):
    queryset=tva_table.objects.all()
    serializer_class= usersSerializer
    pagination_class = MyPagination1
    pagination_class = MyPagination2
    search_fields = ("first_name","last_name")
    ordering_fields = ("id","age")

# For Get Request =======> localhost/users/

class usersCreateAPIView(generics.CreateAPIView):
    queryset=tva_table.objects.all()
    serializer_class= usersSerializer   


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        users = tva_table.objects.get(pk=pk)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = usersSerializer(users)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = usersSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response({},status=status.HTTP_200_OK)

  


































































    
# @api_view(['GET', 'POST'])

# def user_list(request):
#         if request.method=='GET':    
#             userqs = tva_table.objects.all()
#             paginator = MyPagination1()
#             paginator = MyPagination2()
#             filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#             filterset_fields = ('first_name', 'last_name')
#             # filterset = UserFilter(request.GET,queryset=userqs)
#             users_page = paginator.paginate_queryset(userqs,request)
#             serializer = usersSerializer(users_page,many=True)
#             return paginator.get_paginated_response(serializer.data)

#         elif request.method == 'POST':
#             serializer = usersSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class usersCreateAPIView(generics.CreateAPIView):
#     queryset=tva_table.objects.all()
#     serializer_class= usersSerializer

    
# class UserDetailAPIView(generics.RetrieveAPIView):
#     queryset=tva_table.objects.all()
#     serializer_class= usersSerializer
#     lookup_field='id'
    
# class UserUpdateAPIView(generics.UpdateAPIView):
#     queryset=tva_table.objects.all()
#     serializer_class=usersSerializer
#     lookup_field='id'
    
# class UserDeleteAPIView(generics.DestroyAPIView):
#     queryset=tva_table.objects.all()
#     serializer_class=usersSerializer
#     lookup_field='id'

    