from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    uptaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
