from django.db import models
from common.models import CommonModel

# Create your models here.


class Wishlist(CommonModel):

    """Wishlist Model Definition"""

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=150,
    )
    rooms = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="wishlists",
    )
    experiences = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        related_name="wishlists",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )
