# from date_time_utils.
from django.db import models
from django_datetime.date_time import datetime
# store
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Branch(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(default=datetime.dnow())
    updated_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Branches'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.name


# @receiver(post_save, sender=OrderProduct)
# def add(sender, instance, created, **kwargs):
#     pass


# @receiver(post_save, sender=OrderProduct)
# def post_update(sender, instance, **kwargs):
#     pass


@receiver(pre_save, sender=Branch)
def update(sender, instance, **kwargs):
    if instance is None:
        pass
    else:
        if instance.updated_date is None:
            instance.updated_date = datetime.dnow()

# @receiver(post_delete, sender=OrderProduct)
# def delete(sender, instance, using, **kwargs):
#     pass
