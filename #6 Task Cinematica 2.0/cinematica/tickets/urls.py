from django.urls import path
from .views import *


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
    path('club-card', ClubCardView.as_view()),
    path('club-card/<int:pk>', ClubCardDetailView.as_view()),
]
