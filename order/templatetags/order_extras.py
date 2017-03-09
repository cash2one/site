# -*- coding: utf-8 -*-

from django import template

from order.card import ShoppingCart

register = template.Library()


@register.inclusion_tag('order/templatetags/floating_block.html', takes_context=True)
def order_floating_block(context):
    cart = ShoppingCart(context['request'])

    cart_items = cart.get_items()

    cart_item_counter = cart_items.count()
    temp_items = []
    temp_ots = []

    for item in cart.get_items():

        if item.grp == u'н/д' or item.grp == u'':
            continue
        temp_items.append(item.grp.replace(',', '.'))
    cart_item_grp = sum(map(float, temp_items))
    for item in cart.get_items():
        if item.ots == u'н/д' or item.ots == u'':
            continue
        temp_ots.append(item.ots.replace(',', '.'))
    cart_item_ots = sum(map(float, temp_ots))

    return {
        'cart_item_counter': cart_item_counter,
        'cart_item_grp': cart_item_grp,
        'cart_item_ots': cart_item_ots,
    }
