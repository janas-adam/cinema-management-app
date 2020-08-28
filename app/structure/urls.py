from django.urls import path
from django.conf.urls import include
from app.structure.views import (
    AdvertisementCreateView,
    AdvertisementListView,
    AdvertisementUpdateView,
    AdvertisementDeleteView,
    PromotionCreateView,
    PromotionListView,
    PromotionUpdateView,
    PromotionDeleteView,
    PriceCreateView,
    PriceListView,
    PriceUpdateView,
    PriceDeleteView,
    MovieCreateView,
    MovieListView,
    MovieUpdateView,
    MovieDeleteView,
    HallCreateView,
    HallListView,
    HallUpdateView,
    HallDeleteView,
    SeatCreateView,
    SeatListView,
    SeatUpdateView,
    SeatDeleteView,
    ShowCreateView,
    ShowListView,
    ShowUpdateView,
    ShowDeleteView,
)


urlpatterns = [
    path('', AdvertisementListView.as_view(), name='home'),
    path('create-ad', AdvertisementCreateView.as_view(), name='create-ad'),
    path('ad/<int:pk>/update', AdvertisementUpdateView.as_view(), name='update-ad'),
    path('ad/<int:pk>/delete', AdvertisementDeleteView.as_view(), name='delete-ad'),
    path('create-promo', PromotionCreateView.as_view(), name='create-promo'),
    path('promo-list', PromotionListView.as_view(), name='promo-list'),
    path('promo/<int:pk>/update', PromotionUpdateView.as_view(), name='update-promo'),
    path('promo/<int:pk>/delete', PromotionDeleteView.as_view(), name='delete-promo'),
    path('create-price', PriceCreateView.as_view(), name='create-price'),
    path('price-list', PriceListView.as_view(), name='price-list'),
    path('price/<int:pk>/update', PriceUpdateView.as_view(), name='update-price'),
    path('price/<int:pk>/delete', PriceDeleteView.as_view(), name='delete-price'),
    path('create-movie', MovieCreateView.as_view(), name='create-movie'),
    path('movie-list', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/update', MovieUpdateView.as_view(), name='update-movie'),
    path('movie/<int:pk>/delete', MovieDeleteView.as_view(), name='delete-movie'),
    path('create-hall', HallCreateView.as_view(), name='create-hall'),
    path('hall-list', HallListView.as_view(), name='hall-list'),
    path('hall/<int:pk>/update', HallUpdateView.as_view(), name='update-hall'),
    path('hall/<int:pk>/delete', HallDeleteView.as_view(), name='delete-hall'),
    path('create-seat', SeatCreateView.as_view(), name='create-seat'),
    path('seat-list', SeatListView.as_view(), name='seat-list'),
    path('seat/<int:pk>/update', SeatUpdateView.as_view(), name='update-seat'),
    path('seat/<int:pk>/delete', SeatDeleteView.as_view(), name='delete-seat'),
    path('create-show', ShowCreateView.as_view(), name='create-show'),
    path('show-list', ShowListView.as_view(), name='show-list'),
    path('show/<int:pk>/update', ShowUpdateView.as_view(), name='update-show'),
    path('show/<int:pk>/delete', ShowDeleteView.as_view(), name='delete-show'),

]
