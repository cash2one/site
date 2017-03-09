# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType

from order.models import Cart, CartItem
import datetime

CART_ID = 'CART-ID'


class ShoppingCart:
    def __init__(self, request):
        if 'session' in dir(request):
            cart_id = request.session.get(CART_ID)
            if cart_id:
                try:
                    cart = Cart.objects.get(id=cart_id, is_checked_out=False)
                except Cart.DoesNotExist:
                    cart = self.new(request)
            else:
                cart = self.new(request)
            self.cart = cart

    def __iter__(self):
        for item in self.cart.cartitem_set.all():
            yield item

    def new(self, request):
        cart = Cart(created_at=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def get_items(self):
        return CartItem.objects.filter(cart=self.cart)

    def smart_add(self, product):
        return CartItem.objects.get_or_create(
            cart=self.cart,
            object_id=product.id,
            content_type=ContentType.objects.get_for_model(product),
            grp=product.grp,
            ots=product.ots
        )

    def smart_remove(self, product):
        try:
            item = CartItem.objects.get(
                cart=self.cart,
                object_id=product.id,
            )
        except Exception, e:
            pass
        else:
            item.delete()

    def add(self, product, quantity=1):
        return CartItem.objects.create(cart=self.cart, object_id=product.id,
                                       content_type=ContentType.objects.get_for_model(product), grp=product.grp,
                                       ots=product.ots, quantity=quantity)

    def remove(self, pk):
        try:
            item = CartItem.objects.get(
                cart=self.cart,
                pk=pk,
            )
        except CartItem.DoesNotExist:
            raise Exception
        else:
            item.delete()

    def update(self, pk, quantity, relative=False):
        try:
            item = CartItem.objects.get(cart=self.cart, pk=pk)
            if relative:
                item.quantity += int(quantity)
            else:
                item.quantity = quantity
            if item.quantity <= 0:
                self.remove(pk)
                return
            item.save()
        except CartItem.DoesNotExist:
            raise Exception

    def avil(self):
        if self.summary() == 0:
            return False
        return True

    def clear(self):
        for item in self.cart.cartitem_set.all():
            item.delete()

    def quantity(self):
        if 'cart' in self.__dict__:
            result = 0
            for item in self.cart.cartitem_set.all():
                result += item.quantity
            return result

    def count(self):
        return self.cart.cartitem_set.count()

    def summary(self):
        result = 0
        for item in self.cart.cartitem_set.all():
            result += item.total_grp
        return result

    def get_item(self, pk):
        try:
            return CartItem.objects.get(cart=self.cart, pk=pk)
        except CartItem.DoesNotExist:
            raise Exception
