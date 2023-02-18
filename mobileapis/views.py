from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mobileapis.serializer import *
from mobileapis.models import *

# Create your views here.

@api_view(['GET'])
def get_credit(request):
    json_credits = Credit.objects.all()
    serializer_credit = CreditSerializer(json_credits, many=True)
    return Response(serializer_credit.data)


@api_view(['GET'])
def search_credit(request, pk):
    username = request.GET.get('username')
    user = Clent.objects.get(username=username)
    queryset = Credit.objects.filter(id=pk, user=user)
    serializer = CreditSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def delete_credit(request, pk):
    username = request.GET.get('username')
    usr = Clent.objects.get(username=username)
    user = Credit.objects.filter(id=pk, user=usr)
    if user is not None:
        user.delete()
        return Response(f'{usr}ning credit ma\'lumotlari muvaffaqiyatli o\'chirildi')
    else:
        return Response('Xatolik yuz berdi. Qaytadan urinib ko\'ring' ,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_credit(request):
    user = request.POST.get('clent')
    usr = Clent.objects.get(username=user)
    product = request.POST.get('product')
    quantity = int(request.POST.get('quantity'))
    given_price = int(request.POST.get('given_price'))
    amount = int(request.POST.get('amount'))
    model = request.POST.get('model')
    color = request.POST.get('color')
    imei = int(request.POST.get('imei'))
    imei2 = int(request.POST.get('imei2'))
    if len(str(imei)) and len(str(imei2)) <= 16:
        imei += int(imei)
        imei2 += int(imei2)
        description = request.POST.get('description')
        loan_period = int(request.POST.get('loan_period'))
        interest_rate = int(request.POST.get('interest_rate'))
        if usr.status == 0:
            credit = Credit.objects.create(user=usr, product=product, quantity=quantity, given_price=given_price,
                                           amount=amount,
                                           model=model, color=color, imei=imei, imei2=imei2, description=description,
                                           loan_period=loan_period,
                                           interest_rate=interest_rate)
            return Response(f'{usr} uchun credit muvaffaqiyatlik yakunlandi', status=200)
        elif usr.status == 1:
            return Response(f'Credit ushbu user uchun ruxsat berilmagan. {usr} qora ro\'yxatda ', status=403)
    else:
        return Response('imei raqamlari 16 ta raqamdan kam bo\'lishi kerak qaytadan tekshirib ko\'ring')


@api_view(['GET'])
def confirmate(request, pk):
    clent = request.GET.get('clent')
    summa = int(request.GET.get('summa'))
    usr = Clent.objects.get(username=clent)
    credit = Credit.objects.get(id=pk, user=usr)
    val = credit.monthly_payment[1].get('monthly-payment')
    val1 = credit.remaining_amount[1].get('remaining-amount')
    if summa == val:
        checking = credit.remaining_amount
        if len(checking) != 1:
            month = credit.remaining_amount[1].get('month')
            credit.payment(val)
            return Response(f'{credit.user}ning krediti {month}-oyda to\'liq to\'lov bilan yakunlandi')
        elif len(checking) == 1:
            return Response(f'Qolgan miqdor bo\'sh. Qaytadan urinib ko\'ring')
    elif summa == val1:
        checking = credit.remaining_amount
        if len(checking) != 1:
            month = credit.remaining_amount[1].get('month')
            credit.payment(val1)
            return Response(f'{credit.user}ning krediti {month}-oyda to\'liq to\'lov bilan yakunlandi')
        elif len(checking) == 1:
            return Response(f'Qolgan miqdor bo\'sh. Qaytadan urinib ko\'ring')
    else:
        return Response('kiritilgan miqdorda xatolik qaytadan tering')