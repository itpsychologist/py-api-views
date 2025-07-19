from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")

urlpatterns = [
    # Genre routes using APIView functions
    path("genres/", GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),

    # Actor routes using GenericAPIView
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # Include the router URLs for both MovieViewSet and CinemaHallViewSet
    path("", include(router.urls)),
]

app_name = "cinema"
