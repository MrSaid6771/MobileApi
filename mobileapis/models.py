from django.db import models
from account.models import Clent
import jsonfield
from django.utils import timezone


class Credit(models.Model):
    user = models.ForeignKey(Clent, on_delete=models.CASCADE, blank=True, null=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    given_price = models.IntegerField(default=0)
    amount = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    imei = models.IntegerField(unique=True)
    imei2 = models.IntegerField(blank=True)
    description = models.CharField(max_length=255)
    loan_period = models.IntegerField()
    interest_rate = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    monthly_payment = jsonfield.JSONField(blank=True, null=True)
    remaining_amount = jsonfield.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        main_amount = int(self.amount)
        given_price = int(self.given_price)
        interest_rate = int(self.interest_rate)
        loan_period = int(self.loan_period)
        if given_price is not None:
            main_amount -= given_price
        a = [{
            "clent": self.user.username,
            "clent_phone_number": self.user.clent_phone_number,
            "kafil": self.user.kafil,
            "kafil_phone_number": self.user.kafil_phone_number,
        }]
        x = 0
        monthly_payment_1 = (main_amount * (interest_rate / 12)) / ((1 - (1 + (interest_rate / 12))) * (1 - loan_period))
        for i in range(loan_period):
            monthly_interest_rate = (main_amount * ((interest_rate / 100) / 12))
            main_amount -= monthly_payment_1
            x += 1
            a.append({
                "month": x,
                "main-amount": int((monthly_payment_1 - monthly_interest_rate)),
                "interest-accrued": int(monthly_interest_rate),
                "monthly-payment": int(monthly_payment_1),
                "remaining-amount": int(main_amount),
            })
        self.monthly_payment = a
        if self.date_created == self.date_updated:
            self.remaining_amount = a
            self.date_updated = timezone.now()
        else:
            pass
        super(Credit, self).save(*args, **kwargs)

    def payment(self, value, *args, **kwargs):
        remaining_amount = self.remaining_amount
        month1 = remaining_amount[1]
        monthpay = month1.get('monthly-payment')
        remain_amount = month1.get('remaining-amount')
        month = month1.get('month')
        if value <= monthpay:
            if value == monthpay:
                remaining_amount.pop(1)
            else:
                month1.update({'monthly-payment': monthpay - value})
                remaining_amount.insert(1, month1)
        elif value == remain_amount:
            remaining_amount.clear()
            remaining_amount.append({
                "clent": self.user.username,
                'finished-from-month': month,
                'remain-amount': remain_amount
            })

        self.remaining_amount = remaining_amount
        super(Credit, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.user.username} {self.product} {self.quantity} {self.description}'

