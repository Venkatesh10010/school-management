from django.core.signals import request_started, request_finished
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Teacher, TeacherDetail

# #  pre_save → before save
# @receiver(pre_save, sender=Teacher)
# def before_teacher_save(sender, instance, **kwargs):
#     print(f"Before saving Teacher: {instance.name}")
#     if instance.name:
#         instance.name = instance.name.title()   # Example: auto format name
#

# # post_save → after save
@receiver(post_save, sender=Teacher)
def create_teacher_detail(sender, instance, created, **kwargs):
    if created:
        TeacherDetail.objects.create(teacher=instance)
        print(f"TeacherDetail created for {instance.name}")


# #  Before delete (optional)
# @receiver(pre_delete, sender=Teacher)
# def before_teacher_delete(sender, instance, **kwargs):
#     print(f"About to delete Teacher: {instance.name}")
#
# # After delete
# @receiver(post_delete, sender=Teacher)
# def after_teacher_delete(sender, instance, **kwargs):
#     print(f"Teacher deleted: {instance.name}")
#     # Example: also delete related TeacherDetail if still exists
#     TeacherDetail.objects.filter(teacher=instance).delete()
#     print(f"Deleted related TeacherDetail for {instance.name}")




# # 3) request_started and request_finished
# # ---------------------------
# @receiver(request_started)
# def log_request_started(sender, **kwargs):
#     # Fires for each incoming HTTP request (including static/media requests in dev)
#     print("Request started")
#
# @receiver(request_finished)
# def log_request_finished(sender, **kwargs):
#     # Fires after Django finished handling request & response sent
#     print("Request finished")






# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Teacher, TeacherDetail
#
# @receiver(post_save, sender=Teacher)
# def create_teacher_detail_and_send_mail(sender, instance, created, **kwargs):
#     if created:
#         # create detail (avoid duplicates)
#         TeacherDetail.objects.get_or_create(teacher=instance)
#
#         print(f"TeacherDetail created for {instance.name}")
#
#         # send welcome mail if email exists
#         if instance.email:
#             subject = "Welcome to Our App "
#             message = (
#                 f"Hi {instance.name},\n\n"
#                 "Welcome to our app! We're happy to have you onboard.\n\n"
#                 "Regards,\nTeam"
#             )
#             from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "admin@yourapp.com")
#             recipient_list = [instance.email]
#
#             try:
#                 send_mail(subject, message, from_email, recipient_list)
#                 print(f" Welcome mail sent to {instance.email}")
#             except Exception as e:
#                 # for debug in dev — you can log this instead
#                 print(f"Failed to send mail to {instance.email}: {e}")
