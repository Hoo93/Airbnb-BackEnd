from django.db import models

# Create your models here.
class House(models.Model):

    """ Model Definition for houses """
    
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        help_text="Positive numbers only",
        verbose_name="Price"
        )

    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(
        default=True,
        verbose_name="Pets allowed?",
        help_text="Does this house allow pets?")

    def __str__(self):
        return self.name




