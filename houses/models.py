from django.db import models
from users.models import User


class House(models.Model):
    HOUSE_STATUS = (
        ('OM', 'on market'),
        ('SD', 'sold'),
        ('PD', 'pending'),
    )

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    address = models.CharField(
        max_length=300, unique=True, blank=False, null=False)
    zipcode = models.CharField(
        max_length=5, blank=False, null=False)

    status = models.CharField(max_length=2, choices=HOUSE_STATUS, default='OM')

    description = models.TextField()

    owner = models.ForeignKey(
        'users.User', related_name='houses', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('created',)
