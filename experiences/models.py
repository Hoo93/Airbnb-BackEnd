from django.db import models
from common.models import CommonModel

# Create your models here.


class Experience(CommonModel):

    """Experience Model Definition"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=180, default="")

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    addrss = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )


class Perk(CommonModel):
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=180,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default=True,
    )
    explanation = models.TextField(
        blank=True,
        default=True,
    )
