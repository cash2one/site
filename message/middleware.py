# -*- coding: utf-8 -*-

# from message.models import Message, Mail
#
# class MessageMiddleware(object):
#     def process_request(self, request):
#         for message in Message.objects.all():
#             if message.type == 'message_after_activation_email':
#                 request.message_after_activation_email = message.message
#
#             elif message.type == 'message_after_password_reset_email':
#                 request.message_after_password_reset_email = message.message
#
#             elif message.type == 'message_after_successful_authentication':
#                 request.message_after_successful_authentication = message.message
#
#             elif message.type == 'message_after_successful_profile_saving':
#                 request.message_after_successful_profile_saving = message.message
#
#             elif message.type == 'message_after_successful_password_changing':
#                 request.message_after_successful_password_changing = message.message
#
#             elif message.type == 'message_after_adding_the_goods_into_the_basket':
#                 request.message_after_adding_the_goods_into_the_basket = message.message
#
#             elif message.type == 'message_after_successful_order_sending':
#                 request.message_after_successful_order_sending = message.message
#
#             elif message.type == 'message_after_unsuccessful_search':
#                 request.message_after_unsuccessful_search = message.message
#
#             elif message.type == 'error_404':
#                 request.error_404 = message.message
#
#             else:
#                 request.message_after_unsuccessful_filtration = message.message
#
#
# class MailMiddleware(object):
#     def process_request(self, request):
#         for mail in Mail.objects.all():
#             if mail.type == 'activation_email':
#                 request.activation_email = mail
#
#             elif mail.type == 'account_activated_email':
#                 request.account_activated_email = mail
#
#             elif mail.type == 'password_reset_email':
#                 request.password_reset_email = mail
#
#             elif mail.type == 'customer_email':
#                 request.customer_email = mail