from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Libro

@receiver(post_save, sender=User)
def asignar_permiso_desarrollo(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Libro)
        permission = Permission.objects.get(
            codename='development',
            content_type=content_type,
        )
        instance.user_permissions.add(permission)
