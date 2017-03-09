# -*- coding: utf-8 -*-

from django.contrib import admin
from order.models import Order, OrderItem, OrderStatus


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_initial', 'is_closing', 'index_number')
    list_editable = ('is_initial', 'is_closing', 'index_number')
    list_filter = ('is_initial',)

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'is_initial', 'is_closing', 'index_number',)
        }),
    )


admin.site.register(OrderStatus, OrderStatusAdmin)


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


admin.site.register(OrderItem)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'ip', 'company', 'order_items', 'full_name', 'phone', 'total_grp', 'date_start', 'date_end',
                    'status')
    list_editable = ('status',)
    list_filter = ('created_at', 'status')
    inlines = (OrderItemInline,)

    fieldsets = (
        #        (u'Пользователь', {
        #            'classes': ('collapse',),
        #            'fields': ('user',)
        #        }),
        (u'Информация о покупателе', {
            'classes': ('collapse',),
            'fields': ('full_name', 'company', 'phone', 'email', 'ip')
        }),
        (u'Сроки', {
            'classes': ('collapse',),
            'fields': ('date_start', 'date_end'),
        }),
        (u'Статус', {
            'classes': ('collapse',),
            'fields': ('status',),
        }),
        # (u'Дополнительная информация', {
        #     'classes': ('collapse',),
        #     'fields': ('external_id',),
        #     }),
    )

    def order_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        try:
            return ', '.join(["<a href='%s' target='_blank'>%s</a>" % (
                item.passport.get_absolute_url(), item.passport_name
            ) for item in items])
        except:
            return ''

    order_items.short_description = u'Список паспортов'
    order_items.allow_tags = True

    def total_grp(self, obj):
        items = OrderItem.objects.filter(order=obj)
        summary = 0
        temp_item = []
        for item in items:
            if item.grp == u'н/д':
                continue
            temp_item.append(item.grp.replace(',', '.'))
        summary = sum(map(float, temp_item))
        # return str(int(summary))
        return str(summary)

    total_grp.short_description = u'Суммарный коэф. GRP'


admin.site.register(Order, OrderAdmin)

# for item in cart.get_items():
#     if item.grp == u'н/д':
#         continue
#     temp_item.append(item.grp.replace(',', '.'))
# cart_item_grp = sum(map(float, temp_item))
