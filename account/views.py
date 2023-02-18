from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import *
from .serializer import ClentSerializer

@api_view(["GET"])
def get_clent(request):
    users = Clent.objects.all()
    user_serializer = ClentSerializer(users, many=True)
    return Response(user_serializer.data)

@api_view(['GET'])
def search_clent(request, pk):
    username = request.GET.get('username')
    queryset = Clent.objects.filter(id=pk, username=username)
    serializer = ClentSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def delete_clent(request, pk):
    username = request.GET.get('username')
    user = Clent.objects.filter(id=pk, username=username)
    if user is not None:
        user.delete()
        return Response(f'{username} Muvaffaqiyatli o\'chirildi')
    else:
        return Response('Xatolik, qaytadan urinib ko\'ring',status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def update_clent(request, pk):
    username = request.POST.get('username')
    phone_number = request.POST.get('phone_number')
    kafil = request.POST.get('kafil')
    kafil_phone_number = request.POST.get('kafil_phone_number')
    user = Clent(id=pk)
    try:
        user.username = username
        user.save()
    except Exception as ex:
        return Response(ex)
    user.clent_phone_number=phone_number
    user.kafil=kafil
    user.kafil_phone_number=kafil_phone_number
    user.save()
    return Response(f"{user} Muvaffaqiyatli yangilandi")

@api_view(['GET'])
def change_status(request, pk):
    keyword = request.GET.get('keyword')
    user = request.GET.get('user')
    usr = Clent.objects.get(id=pk,username=user)
    if keyword == 'platinum':
        usr.status = 0
        usr.save()
        return Response(f'{usr} muvaffaqqiyatli platinum ro\'yxatiga qo\'shildi')
    elif keyword == 'blacklist':
        usr.status = 1
        usr.save()
        return Response(f'{usr} muvaffaqqiyatli blacklist ro\'yxatiga qo\'shildi')
    else:
        return Response('Kalitso\'z xato. Qayta urinib ko\'ring')

@api_view(['POST'])
def create_clent(request):
    username = request.POST.get('username')
    phone_number = request.POST.get('phone_number')
    kafil = request.POST.get('kafil')
    kafil_phone_number = request.POST.get('kafil_phone_number')
    usr = Clent.objects.create(username=username, clent_phone_number=phone_number,
                                   kafil=kafil, kafil_phone_number=kafil_phone_number)
    usr.save()
    return Response(f'{usr} Muvaffaqqiyatli yaratildi')

