from django.db import models
from django.contrib.auth.models import User
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specifications = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='equipment_images/')

    def __str__(self):
        return self.name




class Booking(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.equipment.name} booked by {self.user.username} from {self.start_date} to {self.end_date}"