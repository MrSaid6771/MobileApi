from django.test import TestCase

# Create your tests here.

# Register API
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def objects_get_method(request):

    # register_pk = Registration.objects.get(pk=pk)
    # # if request.method == 'GET':
    # #
    # #
    # #     serializer_register = RegisterSerializer(register, many=True)
    # #     return Response(serializer_register.data, status=400)
    #
    # elif request.method == 'POST':
    #     request_data = request.data
    #     if 'username' in request_data:
    #         data = request.data
    #         serializer = RegisterSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=404)
    #         return Response(serializer.errors, status=400)
    #     elif 'price' in request_data:
    #         data = request.data
    #         serializer = ForMobileSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=201)
    #         return Response(serializer.errors, status=400)
    #     else:
    #         return Response({"failed": False})
    #
    # elif request.method == 'PUT':
    #     data = request.data
    #     serializer = RegisterSerializer(register_pk, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)
    #
    # elif request.method == "DELETE":
    #     data = request.data
    #     serializer = RegisterSerializer(register_pk, data=data)
    #     if serializer.is_valid():
    #         serializer()
    #     return Response(status=400)

# class MobileImg(models.Model):
#     photo = models.ImageField(upload_to='mobile_img/')
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class SubCategory(models.Model):
#     name = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


# @api_view(['POST'])
# def calculate_info(request, pk):
#     username = User.objects.get(id=pk)
#     amount = int(request.POST.get('hisob'))
#     loan_period = int(request.POST.get('qarz_muddati'))
#     interest_rate = int(request.POST.get('stavka_foizi'))
#     Credit.objects.create(username= username, amount=amount,
#                           loan_period=loan_period,
#                           interest_rate=interest_rate)
#     return Response(' Successfully saved')



# @api_view(['DELETE'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_user(request):
#     user = request.user
#     user.delete()
#     return Response('Deleted')

#
# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def index(request):
#     if request.user.status == 3:
#         users = User.objects.all()
#         print(request.user.mobile.name)
#         return Response('successfully')
#     elif request.user.status == 0:
#         return Response('zapret')




# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from account.models import User
# import jsonfield

# class Color(models.Model):
#     color = models.CharField(unique=True, max_length=255)
#
#     def __str__(self):
#         return self.color
#
#
# class Brand(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class MobileName(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


# class Mobile(models.Model):
#     model = models.ForeignKey(MobileName, on_delete=models.CASCADE, related_name='mobile', blank=True)
#     price = models.IntegerField()
#     color = models.ForeignKey(Color, on_delete=models.CASCADE)
#     imei = models.IntegerField(unique=True)
#     imei2 = models.IntegerField(blank=True)
#     description = models.CharField(max_length=255)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.model.name} {self.description} {self.color}'


# class Credit(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.OneToOneField(Mobile, on_delete=models.CASCADE, null=True, blank=True)
#     given_price = models.IntegerField()
#     amount = models.IntegerField(blank=True, null=True)
#     loan_period = models.IntegerField()
#     interest_rate = models.IntegerField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     monthly_payment = jsonfield.JSONField(blank=True, null=True)
#
#
#     def save(self, *args, **kwargs):
#         self.amount = self.product.price
#         if self.given_price is not None:
#             self.amount -= self.given_price
#         main_amount = int(self.amount)
#         a = []
#         x = 0
#         monthly_payment_1 = (self.amount * (self.interest_rate / 12)) / ((1 - (1 + (self.interest_rate / 12))) * (1 - self.loan_period))
#         for i in range(self.loan_period):
#             monthly_interest_rate = (main_amount * ((self.interest_rate / 100) / 12))
#             main_amount -= monthly_payment_1
#             x += 1
#             a.append({
#                 "month": x,
#                 'xx': monthly_interest_rate,
#                 "Main amount": (monthly_payment_1 - monthly_interest_rate),
#                 "Interest accrued": monthly_interest_rate,
#                 "Monthly_payment": monthly_payment_1,
#                 "Remaining amount": main_amount,
#             })
#         self.monthly_payment = a
#         super(Credit, self).save(*args, **kwargs)
#
#



    # def payment(self, summa):
    #     print(self.monthly_payment[0])
    #     a = self.monthly_payment[1].get("Monthly_payment")
    #     while summa >= a:
    #         if self.monthly_payment[0].get("Monthly_payment") == summa:
    #             self.monthly_payment.pop(0)
    #         else:
    #             summa -= self.monthly_payment[0].get("Monthly_payment")
    #             self.monthly_payment.pop(0)
    #     qwer = self.monthly_payment[0].get("Monthly_payment")
    #     qwer -= summa
    #     self.monthly_payment[0].update(Monthly_payment=qwer)
    #     super(Credit, self).save(summa)


    # def __str__(self):
    #     return f'{self.user.username}'



#
# @api_view(['GET'])
# def get_mobile(request):
#     mobile = Mobile.objects.all()
#     mobile_serializer = Mobileserializer(mobile, many=True)
#     return Response(mobile_serializer.data)


# @api_view(['POST'])
# def create_product(request):
#     quantity = request.POST.get('miqdori')
#     nomi = request.POST.get('nomi')
#     narx = int(request.POST.get('narx'))
#     model = request.POST.get('model')
#     imeika = int(request.POST.get('imeka'))
#     imei_second = int(request.POST.get('imei_second'))
#     Mobile.objects.create(name=nomi, price=narx, model=model,
#                           imei=imeika, imei_second=imei_second, quantity=quantity)
#     return Response('success')


# @api_view(['POST'])
# def create_color(request):
#     color = request.POST.get('color')
#     if color is not None:
#         Color.objects.create(color=color)
#         return Response('success created')
#     else:
#         return Response('Check please')





# @api_view(['GET'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_product(request):
#     product_name = request.GET.get('name')
#     imei = request.GET.get('imeika')
#     product = Mobile.objects.filter(name=product_name, imei=imei)
#     if product:
#         product.delete()
#     return Response({"Successful deleted"})
#
#
# @api_view(['PUT'])
# @authentication_classes([BasicAuthentication])
# def update_user(request, pk):
#     quantity = request.POST.get('miqdori')
#     nomi = request.POST.get('nomi')
#     narx = int(request.POST.get('narx'))
#     model = request.POST.get('model')
#     imeika = int(request.POST.get('imeka'))
#     imei_second = int(request.POST.get('imei_second'))
#     user = Mobile.objects.create(id=pk, name=nomi, price=narx, model=model,
#                           imei=imeika, imei_second=imei_second, quantity=quantity)
#     user.save()
#     return Response("successful updated")


# monthly_interest_rate = (main_amount * (interest_rate / 100))
# monthly_payment = main_amount / loan_period
# remaining_amount = main_amount - monthly_payment
# interest_rate = interest_rate / loan_period


# def save(self, *args, **kwargs):
#     main_amount = int(self.amount)
#     given_price = int(self.given_price)
#     interest_rate = int(self.interest_rate)
#     loan_period = int(self.loan_period)
#     if given_price is not None:
#         main_amount -= given_price
#     a = [{
#         "Clent": self.user.username,
#         "Clent_phone_number": self.user.clent_phone_number,
#         "Kafil": self.user.kafil,
#         "kafil_phone_number": self.user.kafil_phone_number,
#     }]
#     x = 0
#     monthly_payment_1 = (main_amount * (interest_rate / 12)) / ((1 - (1 + (interest_rate / 12))) * (1 - loan_period))
#     for i in range(loan_period):
#         monthly_interest_rate = (main_amount * ((interest_rate / 100) / 12))
#         main_amount -= monthly_payment_1
#         x += 1
#         a.append({
#             "month": x,
#             "main-amount": int((monthly_payment_1 - monthly_interest_rate)),
#             "interest-accrued": int(monthly_interest_rate),
#             "monthly-payment": int(monthly_payment_1),
#             "remaining-amount": int(main_amount),
#         })
#     self.monthly_payment = a
#     if self.date_created == self.date_updated:
#         self.remaining_amount = a
#         self.date_updated = timezone.now()
#     else:
#         pass
#     super(Credit, self).save(*args, **kwargs)
#
#
# def __str__(self):
#     return f'{self.user.username} {self.product} {self.quantity} {self.description}'

# data = request.data
# serializer = CreditSerializer(data=data)
# if not serializer.is_valid():
#     return Response({status: 200, 'data': serializer, 'message': 'Xatolik yuz berdi'})
# else:
#     serializer.save()
#     return Response({'status': 200, 'data': serializer.data, 'message': 'succes'})

# def full_amount(self, value, *args, **kwargs):
#     remaining_amount = self.remaining_amount
#     if value == remaining_amount[1].get('remaining-amount'):
#         month = remaining_amount[1].get('month')
#         remain_amount = remaining_amount[1].get('remaining-amount')
#         remaining_amount.clear()
#         remaining_amount.append({
#             'month': month,
#             'remain_amount': remain_amount
#         })
#     self.remaining_amount = remaining_amount
#     super(Credit, self).save(*args, **kwargs)
