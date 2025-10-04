from django.db import models

class Ticket(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    depart_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    airline = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin} -> {self.destination} | {self.depart_date} | ${self.price}"
