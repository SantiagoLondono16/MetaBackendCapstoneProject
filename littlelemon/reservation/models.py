from django.db import models

# Create your models here.
class Reservation(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return f"Booking by {self.Name} on {self.BookingDate}"

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{str(self.Title)} : {str(self.Price)}'