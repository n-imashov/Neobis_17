from rest_framework import generics

from users.permissions import (
    IsAdminOrReadOnly,
)
from .serializers import (
    TicketSerializer,
    OrdersSerializer,
    FeedbackSerializer,
    BookingSerializer,
    SeatsSerializer,
    ClubCardSerializer,
    TicketTypeSerializer,
)
from .models import (
    Tickets,
    Orders,
    Feedback,
    Booking,
    Seats,
    ClubCard,
    TicketType,
)


class TicketsView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Tickets.objects.all()


class TicketsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Tickets.objects.all()


class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class FeedbackView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Booking.objects.all()


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Booking.objects.all()


class SeatsView(generics.ListCreateAPIView):
    serializer_class = SeatsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Seats.objects.all()


class SeatsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SeatsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Seats.objects.all()


class TicketTypeView(generics.ListCreateAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()


class TicketTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()


class ClubCardView(generics.ListCreateAPIView):
    serializer_class = ClubCardSerializer
    queryset = ClubCard.objects.all()


class ClubCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubCardSerializer
    queryset = ClubCard.objects.all()
