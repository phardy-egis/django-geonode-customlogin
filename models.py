from django.db import models

class App(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Application name',
        blank=False,
        null=False,
    )
    description = models.CharField(
        max_length=300,
        verbose_name='Application description',
        blank=False,
        null=False
    )
    url = models.URLField(
        verbose_name='URL of application location',
        blank=False,
        null=False
    )

    def __str__(self) -> str:
        return self.name