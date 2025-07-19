from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreListAPIView,
    GenreDetailAPIView,
    ActorListView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")

urlpatterns = [
    # Genre routes using APIView functions
    path("genres/", GenreListAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),

    # Actor routes using GenericAPIView
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),

    # Include the router URLs for both MovieViewSet and CinemaHallViewSet
    path("", include(router.urls)),
]