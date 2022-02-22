# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from django.contrib.auth.models import User
# from .models import Person
#
#
# @receiver(post_save, sender=User)
# def create_person(sender, instance, created, **kwargs):
#     if created:
#         Person.objects.create(user=instance)
#         print('----------------------------------Profile Created--------------------------------------')
#
#
# @receiver(post_save, sender=User)
# def update_person(sender, instance, created, **kwargs):
#     if not created:
#         instance.person.save()
#         print('------------------Profile Updated-----------------------')
