from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import movie_listAV,movie_detailAV

urlpatterns = [
    # path('',movie_list, name='movie-list'),
    # path('<int:pk>',movie_details, name='movie-detail'),
    path('',movie_listAV.as_view(), name='movie-list'),
    path('<int:pk>',movie_detailAV.as_view(), name='movie-detail'),
]