from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class SingletonModel(models.Model):
    """
    Modelo base para crear un singleton. Este modelo asegura que solo haya una instancia de la clase en la base de datos.
    Se utiliza para almacenar configuraciones o datos únicos que no deben repetirse.
    """
    class Meta:
        abstract = True  # Esta clase es abstracta, no genera una tabla en la base de datos.

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise Exception(f'No se puede crear más de una instancia de {self.__class__.__name__}')
        return super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class BaseModel(models.Model):
    """
    Modelo base que contiene información común para el seguimiento de creación y modificación de registros.
    """
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='%(class)s_creados',
        null=True,
        blank=True,
        editable=False
    )
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )
    fecha_creacion = models.DateTimeField(
        default=timezone.now,
        help_text="Data de creació",
        editable=False
    )
    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        help_text="Data de modificació",
        editable=False
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)