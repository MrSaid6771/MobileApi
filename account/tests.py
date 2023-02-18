from django.test import TestCase

# Create your tests here.
# class User(AbstractUser):
#     phone_number = models.CharField(max_length=50, blank=True, null=True)
#     kafil = models.CharField(max_length=50, blank=True, null=True)
#     kafil_phone_number = models.CharField(max_length=50)
#     status = models.IntegerField(default=0, choices=(
#         (0, 'Client'),
#         (1, 'Super admin'),
#     ))
#
#     class Meta(AbstractUser.Meta):
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.response import Response
# from django.contrib.auth import login, logout, authenticate
# from account.models import *
# from .serializer import UserSerializer
#
#
# @api_view(["GET"])
# def get_user(request):
#     users = Clent.objects.all()
#     user_serializer = UserSerializer(users, many=True)
#     return Response(user_serializer.data)
#
#
# @api_view(['POST'])
# def sign_up(request):
#     username = request.POST.get('username')
#     phone_number = request.POST.get('phone_number')
#     kafil = request.POST.get('kafil')
#     kafil_phone_number = request.POST.get('kafil_phone_number')
#     usr = Clent.objects.create_user(username=username, clent_phone_number=phone_number,
#                                    kafil=kafil, kafil_phone_number=kafil_phone_number)
#     usr.save()
#     if usr is not None:
#         login(request, usr)
#         return Response(' successfully signed up ')
#     else:
#         return Response(status=404)
#
#
# @api_view(['POST'])
# def log_in(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     usr = authenticate(username=username, password=password)
#     if usr is not None:
#         login(request, usr)
#         return Response(' successfully loged in ')
#     else:
#         return Response('username or password incorrect, please try again')
#
#
# @api_view(['POST'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_user(request):
#     password = request.POST.get('password')
#     user = request.user
#     if user.check_password(password):
#         user.delete()
#         return Response({"Successful deleted"})
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# def update_user(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     password1 = request.POST.get('password1')
#     phone_number = request.POST.get('phone_number')
#     kafil = request.POST.get('kafil')
#     kafil_phone_number = request.POST.get('kafil_phone_number')
#     user = request.user
#     try:
#         user.username = username
#         user.save()
#     except Exception as ex:
#         return Response(ex)
#     if password1 == password:
#         user.set_password(password)
#         user.save()
#     else:
#         return Response('Parollar bir xil emas')
#     user.phone_number=phone_number
#     user.kafil=kafil
#     user.kafil_phone_number=kafil_phone_number
#     user.save()
#     return Response("successful updated")
#
#
# @api_view(['GET'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def log_out(request):
#     logout(request)
#     return Response('success')


# def search_clent(request, pk):
#     username = request.POST.get('username')
#     queryset = Clent.objects.all()
#     if request.POST == queryset.username:
#         search = queryset.filter(id=pk,username=username)
#         serializer = ClentSerializer(search, many=True)
#         return Response(serializer.data, status=200)
#         # else:
#         #     return Response('sending is failed', status=500)
#     else:
#         return Response('username is not equel', status=404)