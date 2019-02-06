from django.db.models import *
from localflavor.us.models import USZipCodeField, USStateField
from django.contrib.auth import get_user_model

User = get_user_model()

class PaintAdditive(Model):
    name = CharField(max_length=20)
    cost = DecimalField(decimal_places=2, max_digits=6)

class Paint(Model):
    color = IntegerField()
    additives = ManyToManyField(PaintAdditive)

class NamedPaint(Model):
    name = CharField(max_length=30)
    paint = ForeignKey(Paint, on_delete=PROTECT)

class Palette(Model):
    name = CharField(max_length=30)
    paints = ManyToManyField(NamedPaint)

class ShippingInfo(Model):
    name = CharField(max_length=30)
    address1 = CharField(max_length=30)
    address2 = CharField(max_length=30)
    state = USStateField()
    zip = USZipCodeField()

class PaymentInfo(Model):
    pass

class Order(Model):
    shipping = ForeignKey(ShippingInfo, on_delete=PROTECT)
    payment = ForeignKey(PaymentInfo, on_delete=PROTECT)
    user = ForeignKey(User, on_delete=PROTECT)

class OrderItem(Model):
    paint = ForeignKey(NamedPaint, on_delete=PROTECT)
    quantity = PositiveSmallIntegerField()
    order = ForeignKey(Order, on_delete=PROTECT)