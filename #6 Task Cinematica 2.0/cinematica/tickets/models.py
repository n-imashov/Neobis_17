from django.db import models

from movies.models import (
    ShowTime,
    Rooms,
    MovieFormat,
    RoomsFormat,
)
from users.models import User


class Seats(models.Model):
    number_of_seat = models.IntegerField()
    number_of_row = models.IntegerField()
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return f"row:{self.number_of_row }/seat:{self.number_of_seat}"


class TicketType(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tickets(models.Model):
    methods = [
        (1, 'Bank-card'),
        (2, 'Balance.kg'),
        (3, 'Элсом'),
    ]
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    seats = models.ForeignKey(Seats, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ForeignKey("Orders", on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    payment_methods = models.IntegerField(choices=methods)
    club_card = models.ForeignKey("ClubCard", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        price = (
                self.ticket_type.price + \
                self.show_time.movie_format.price + \
                self.seats.rooms.format.price
        )
        if (
                self.ticket_type.name == "adult" or
                self.ticket_type.name == "child" or
                self.ticket_type.name == "student" and
                self.show_time.movie_format.name == '3-D' or
                self.show_time.movie_format.name == '3-2' and
                self.seats.rooms.format.name == 'small' or
                self.seats.rooms.format.name == 'middle' or
                self.seats.rooms.format.name == 'big' or
                self.seats.rooms.format.name == 'Imax'
        ):
            if self.club_card.discount == 0:
                self.price = price
            else:
                price_with_discount = (
                    price / 100 * self.club_card.discount
                )
                self.price = (
                    price - price_with_discount
                )

        super().save(*args, **kwargs)


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


class Feedback(models.Model):
    rates = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    rate = models.IntegerField(choices=rates, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Booking(models.Model):
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seats = models.ForeignKey(Seats, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ClubCard(models.Model):
    balance = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
