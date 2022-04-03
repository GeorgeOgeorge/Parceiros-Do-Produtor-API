from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Base(models.Model):
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Farmer(Base):
    name = models.CharField(blank=False, max_length=255)
    age = models.PositiveSmallIntegerField(blank=False)
    cpf = models.CharField(blank=False,  max_length=11, unique=True)
    phone = models.CharField(blank=False, max_length=11, unique=True)
    sex = models.CharField(blank=False, max_length=11, unique=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'farmer'
        verbose_name_plural = 'farmers'

    def __str__(self):
        return f"{self.name} - {self.cpf}"


class Propertie(Base):
    farmer = models.ForeignKey(
        Farmer,
        related_name='properties',
        on_delete=models.CASCADE
    )
    name = models.CharField(blank=False, max_length=255)
    size = models.DecimalField(blank=False, max_digits=100, decimal_places=1)
    phone = models.CharField(blank=False, max_length=11, unique=True)
    longitude = models.DecimalField(blank=False, decimal_places=16, max_digits=1000)
    latitude = models.DecimalField(blank=False, decimal_places=16, max_digits=1000)

    class Meta:
        ordering = ['id']
        verbose_name = 'propertie'
        verbose_name_plural = 'properties'
        unique_together = ['id', 'farmer']

    def __str__(self):
        return f'the {self.name} propertie is owned by {self.farmer.name}'

class Herd(Base):
    propertie = models.ForeignKey(
        Propertie,
        related_name='herds',
        on_delete=models.CASCADE
    )
    name = models.CharField(blank=False, max_length=255)
    animal_type = models.CharField(blank=False, max_length=255)
    warning = models.BooleanField(blank=False)
    log = models.CharField(blank=False, max_length=255)
    identified_animals = models.BooleanField(blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'herd'
        verbose_name_plural = 'herds'
        unique_together = ['id', 'propertie']

    def __str__(self):
        return f'{self.name} belongs to the {self.propertie.name} property'

class Animal(Base):
    herd = models.ForeignKey(
        Herd,
        related_name='animals',
        on_delete=models.CASCADE
    )
    name = models.CharField(blank=False, max_length=255)
    sex = models.CharField(blank=False, max_length=11, unique=False)
    breed = models.CharField(blank=False, max_length=255)
    code = models.DecimalField(blank=False, max_digits=100, decimal_places=1)
    furr_color = models.CharField(blank=False, max_length=100)
    purchased = models.BooleanField(blank=False)
    birth_date = models.CharField(blank=False, max_length=10)

    class Meta:
        ordering = ['id']
        verbose_name = 'animal'
        verbose_name_plural = 'animals'
        unique_together = ['id', 'herd']

    def __str__(self):
        return f'{self.name} belongs to the {self.herd.name} herd'


class Milking(Base):
    animal = models.ForeignKey(
        Animal,
        related_name='milkings',
        on_delete=models.CASCADE
    )
    value = models.FloatField(blank=False)
    date = models.CharField(blank=False, max_length=11, unique=False)
    shift = models.CharField(blank=False, max_length=100)
    dry = models.BooleanField(blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'milking'
        verbose_name_plural = 'milkings'
        unique_together = ['id', 'animal']

    def __str__(self):
        return f'{self.name} animal has produced {self.value} amount'

