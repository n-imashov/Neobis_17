from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(**kwargs):
    print("Пользователь создан")