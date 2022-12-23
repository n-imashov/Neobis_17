from django.urls import path

from .views import (
    TicketsView,
    TicketsDetailView,
    OrdersView,
    OrdersDetailView,
    FeedbackView,
    FeedbackDetailView,
    BookingView,
    BookingDetailView,
    SeatsView,
    SeatsDetailView,
    TicketTypeView,
    TicketTypeDetailView,
    ClubCardView,
    ClubCardDetailView,
)


urlpatterns = [
    path('tickets', TicketsView.as_view()),
    path('tickets/<int:pk>', TicketsDetailView.as_view()),
    path('orders', OrdersView.as_view()),
    path('orders/<int:pk>', OrdersDetailView.as_view()),
    path('feedbacks', FeedbackView.as_view()),
    path('feedbacks/<int:pk>', FeedbackDetailView.as_view()),
    path('bookings', BookingView.as_view()),
    path('bookings/<int:pk>', BookingDetailView.as_view()),
    path('seats', SeatsView.as_view()),
    path('seats/<int:pk>', SeatsDetailView.as_view()),
    path('type', TicketTypeView.as_view()),
    path('type/<int:pk>', TicketTypeDetailView.as_view()),
    path('club-card', ClubCardView.as_view()),
    path('club-card/<int:pk>', ClubCardDetailView.as_view()),
]