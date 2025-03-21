from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    genre_list,
    genre_detail,
    ActorListView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    # Genre routes using @api_view functions
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),

    # Actor routes using GenericAPIView
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),

    # Include the router URLs for both MovieViewSet and CinemaHallViewSet
    path("", include(router.urls)),
]
