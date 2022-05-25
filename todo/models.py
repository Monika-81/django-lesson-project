from django.db import models

# Create your models here.


class Item(models.Model):
    # prevents items created without a name
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name

