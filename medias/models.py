from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):
    def __str__(self):
        return "Photo File"

    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )


class Video(CommonModel):
    def __str__(self):
        return "Video File"

    file = models.ImageField()

    experince = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )
