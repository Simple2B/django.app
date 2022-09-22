import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Post


logger = logging.getLogger('django')


@receiver(post_save, sender=Post)
def post_save(sender, instance, **kwargs):
    logger.info(f'Post: {instance.title} saved')


@receiver(post_delete, sender=Post)
def post_delete(sender, instance, **kwargs):
    logger.info(f'Post: {instance.title} deleted')
