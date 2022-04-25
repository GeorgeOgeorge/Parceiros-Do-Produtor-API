from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Farmer(AbstractUser):

    active = models.BooleanField(default=True)
    age = models.PositiveSmallIntegerField(blank=True, default=18)
    cpf = models.CharField(max_length=11, unique=True, default='')
    phone = models.CharField(blank=True, max_length=11, unique=True, default='')
    sex = models.CharField(blank=True, max_length=11, unique=False, default='')

    class Meta:
        ordering = ['id']
        verbose_name = 'farmer'
        verbose_name_plural = 'farmers'

    def __str__(self):
        return self.username

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Property(models.Model):

    name = models.CharField(blank=False, max_length=255)
    size = models.DecimalField(blank=False, max_digits=100, decimal_places=1)
    phone = models.CharField(blank=False, max_length=11, unique=True)
    longitude = models.DecimalField(blank=False,decimal_places=16,max_digits=1000)
    latitude = models.DecimalField(blank=False,decimal_places=16,max_digits=1000)
    
    farmer = models.ForeignKey(
        Farmer,
        related_name='property_farmer',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'property'
        verbose_name_plural = 'properties'
        unique_together = ['id', 'farmer']

    def __str__(self):
        return f'the {self.name} property is owned by {self.farmer.username}'


class Production(models.Model):

    active = models.BooleanField(default=True)
    name = models.CharField(blank=False, max_length=255)
    animal_type = models.CharField(blank=False, max_length=255)
    warning = models.BooleanField(blank=False)
    log = models.CharField(blank=False, max_length=255)
    identified_animals = models.BooleanField(blank=False)

    property = models.ForeignKey(
        Property,
        related_name='production_property',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'production'
        verbose_name_plural = 'productions'
        unique_together = ['id', 'property']

    def __str__(self):
        return f'{self.name} belongs to the {self.property.name} property'


class Animal(models.Model):

    active = models.BooleanField(default=True)
    name = models.CharField(blank=False, max_length=255)
    sex = models.CharField(blank=False, max_length=11, unique=False)
    breed = models.CharField(blank=False, max_length=255)
    code = models.DecimalField(blank=False, max_digits=100, decimal_places=1)
    furr_color = models.CharField(blank=False, max_length=100)
    purchased = models.BooleanField(blank=False)
    birth_date = models.CharField(blank=False, max_length=10)

    production = models.ForeignKey(
        Production,
        related_name='animal_production',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'animal'
        verbose_name_plural = 'animals'
        unique_together = ['id', 'production']

    def __str__(self):
        return f'{self.name} belongs to the {self.production.name} production'


class Milking(models.Model):

    active = models.BooleanField(default=True)
    value = models.FloatField(blank=False)
    date = models.CharField(blank=False, max_length=11, unique=False)
    shift = models.CharField(blank=False, max_length=100)
    dry = models.BooleanField(blank=False)

    animal = models.ForeignKey(
        Animal,
        related_name='milking_animal',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'milking'
        verbose_name_plural = 'milkings'
        unique_together = ['id', 'animal']

    def __str__(self):
        return f'{self.animal.name} animal has produced {self.value} amount'
