from django.db.models import signals
from django.dispatch import receiver
from apps.users.models import User, UserCart, Address


@receiver(signals.post_save, sender=User)
def cart_creator(sender, instance: User, created, **kwargs):
    if created:
        UserCart.objects.create(user=instance)


@receiver(signals.post_save, sender=Address)
def default_address_update(sender, instance: Address, created, **kwargs):
    if instance.default:
        Address.objects.filter(user=instance.user).exclude(id=instance.id).update(default=False)
