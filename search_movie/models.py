from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_password = models.CharField(max_length=200, null=True)
    user_name = models.CharField(max_length=200, null=True)
    user_phone = models.IntegerField(default=0)
    user_email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user_name


class City(models.Model):
    city_name = models.CharField(max_length=200, null=True)
    city_state = models.CharField(max_length=200, null=True)
    city_pin_code = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name


class Cinema(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    cinema_name = models.CharField(max_length=200, null=True)
    cinema_screens = models.IntegerField(default=0)

    def __str__(self):
        return self.cinema_name


class Screen(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True)
    screen_name = models.CharField(max_length=200, null=True)
    screen_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.screen_name


class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, blank=True, null=True)
    seat_number = models.CharField(max_length=10, null=True)
    seat_type = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.seat_number
