# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Materiales(models.Model):

    #__Materiales_FIELDS__
    codigo = models.CharField(max_length=255, null=True, blank=True)
    cas = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    situacionmercado = models.CharField(max_length=255, null=True, blank=True)
    stock = models.TextField(max_length=255, null=True, blank=True)

    #__Materiales_FIELDS__END

    class Meta:
        verbose_name        = _("Materiales")
        verbose_name_plural = _("Materiales")


class Proveedores(models.Model):

    #__Proveedores_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)

    #__Proveedores_FIELDS__END

    class Meta:
        verbose_name        = _("Proveedores")
        verbose_name_plural = _("Proveedores")


class Compras(models.Model):

    #__Compras_FIELDS__
    buyer = models.CharField(max_length=255, null=True, blank=True)
    materia = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    estatus = models.CharField(max_length=255, null=True, blank=True)
    comentarios = models.CharField(max_length=255, null=True, blank=True)
    solicitud = models.CharField(max_length=255, null=True, blank=True)
    fechainicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fechalimite = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fechaentregaprevista = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tipocompra = models.CharField(max_length=255, null=True, blank=True)
    costetransporte = models.CharField(max_length=255, null=True, blank=True)

    #__Compras_FIELDS__END

    class Meta:
        verbose_name        = _("Compras")
        verbose_name_plural = _("Compras")


class Contratos(models.Model):

    #__Contratos_FIELDS__
    kg = models.CharField(max_length=255, null=True, blank=True)
    proveedor = models.CharField(max_length=255, null=True, blank=True)
    contratoid = models.CharField(max_length=255, null=True, blank=True)

    #__Contratos_FIELDS__END

    class Meta:
        verbose_name        = _("Contratos")
        verbose_name_plural = _("Contratos")



#__MODELS__END
